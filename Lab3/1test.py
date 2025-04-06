from tkinter import font
import pygame
import sys

pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15

# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Board size
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(WHITE)

board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]  #list comprehension for storing game data

def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, BLACK, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)

def mark_square(row, col, _player):
    board[row][col] = _player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(_player):
    # Vertical win
    for col in range(BOARD_COLS):
        if board[0][col] == _player and board[1][col] == _player and board[2][col] == _player:
            print(f"Vertical win on column {col} by player {_player}")
            draw_vertical_winning_line(col)
            return True

    # Horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0] == _player and board[row][1] == _player and board[row][2] == _player:
            print(f"Horizontal win on row {row} by player {_player}")
            draw_horizontal_winning_line(row)
            return True

    # Ascending diagonal win
    if board[2][0] == _player and board[1][1] == _player and board[0][2] == _player:
        print(f"Ascending diagonal win by player {_player}")
        draw_asc_diagonal()
        return True

    # Descending diagonal win
    if board[0][0] == _player and board[1][1] == _player and board[2][2] == _player:
        print(f"Descending diagonal win by player {_player}")
        draw_desc_diagonal()
        return True

    return False

def draw_vertical_winning_line(col):
    pos_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = BLACK
    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, HEIGHT - 15), WIN_LINE_WIDTH)


def draw_horizontal_winning_line(row):
    pos_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = BLACK
    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), WIN_LINE_WIDTH)


def draw_asc_diagonal():
    color = BLACK
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)


def draw_desc_diagonal():
    color = BLACK
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // 100, x // 100
            index = row * 3 + col

            # If the cell is empty, make a move
            if board[index] == " ":
                board[index] = current_player

                # Check for win or draw
                if check_win():
                    game_over = True
                # elif check_draw():
                #     game_over = True

                # Switch player
                current_player = "O" if current_player == "X" else "X"

    # Draw the board
    draw_lines()
    draw_figures()

    # Show game over message
    if game_over:
        winner = check_win()
        if winner:
            text = font.render(f"{winner} Wins!", True, LINE_COLOR)
        else:
            text = font.render("It's a Draw!", True, LINE_COLOR)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()  # Update the display