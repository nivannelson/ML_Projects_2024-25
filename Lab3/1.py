# Develop a two-player tic-tac-toe game using pygame

import pygame
import sys
# Screen size
WIDTH, HEIGHT = 400, 600
LINE_WIDTH = 15

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# Color definitions
WHITE = (255, 255, 255)
REST_GRAY=(241,241,241)
HOVER_GRAY=(231,231,231)
CLICK_GRAY=(200,200,200)
GREY= (211,211,211)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# Board size

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_COLOR = (50, 50, 50)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_FONT = pygame.font.Font(None, 30)

reset_button_rect = pygame.Rect(
    (WIDTH - BUTTON_WIDTH) // 2,
    (HEIGHT - BUTTON_HEIGHT) // 2+250,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
)
font = pygame.font.Font(None, 50)
win = pygame.display.set_mode((WIDTH, HEIGHT))
text = font.render("It's a Tie!", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
win.blit(text, text_rect)

board = [['' for _ in range(3)] for _ in range(3)]
flag='X'
status='Ready'
rest=0

def check_game_status(gboard):
    # Determine whose turn it is
    global status
    x_count = sum(row.count('X') for row in gboard)
    o_count = sum(row.count('O') for row in gboard)

    if x_count <= o_count:  # Player 1's turn
        status = "Player 1's turn"
    else:  # Player 2's turn
        status = "Player 2's turn"

    # Check rows for win
    for row in gboard:
        if row[0] == row[1] == row[2] != '':
            status = f"Player {row[0]} wins"
            return  # Stop further checks if there's a winner

    # Check columns for win
    for col in range(3):
        if gboard[0][col] == gboard[1][col] == gboard[2][col] != '':
            status = f"Player {gboard[0][col]} wins"
            return  # Stop further checks if there's a winner

    # Check diagonals for win
    if gboard[0][0] == gboard[1][1] == gboard[2][2] != '':
        status = f"Player {gboard[0][0]} wins"
        return  # Stop further checks if there's a winner
    if gboard[0][2] == gboard[1][1] == gboard[2][0] != '':
        status = f"Player {gboard[0][2]} wins"
        return  # Stop further checks if there's a winner

    # Check for draw (if there are no empty spaces left and no winner)
    empty_spaces = sum(row.count('') for row in gboard)
    if empty_spaces == 0:
        status = "Draw"

class Button(pygame.sprite.Sprite):
    # 1) no need to have 4 parameters for position and size, use pygame.Rect instead
    # 2) let the Button itself handle which color it is
    # 3) give a callback function to the button so it can handle the click itself
    def __init__(self, color, color_hover,color_press, rect, callback, text='', outline=None,index=[0,0]):
        super().__init__()
        
        self.row,self.col=index
        self.text = text
        # a temporary Rect to store the size of the button
        tmp_rect = pygame.Rect(0, 0, *rect.size)
 
        # create two Surfaces here, one the normal state, and one for the hovering state
        # we create the Surfaces here once, so we can simple built them and dont have
        # to render the text and outline again every frame
        self.org = self._create_image(color, outline, self.text, tmp_rect)
        self.hov = self._create_image(color_hover, outline, self.text, tmp_rect)
        self.press = self._create_image(color_press, outline, self.text, tmp_rect)
 
        # in Sprites, the image attribute holds the Surface to be displayed...
        self.image = self.org
        # ...and the rect holds the Rect that defines it position
        self.rect = rect
    def _create_image(self, color, outline, text, rect):
        # function to create the actual surface
        # see how we can make use of Rect's virtual attributes like 'size'
        img = pygame.Surface(rect.size)
        if outline:
            # here we can make good use of Rect's functions again
            # first, fill the Surface in the outline color
            # then fill a rectangular area in the actual color
            # 'inflate' is used to 'shrink' the rect
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -3))
        else:
            img.fill(color)
 
        # render the text once here instead of every frame  
        # if text != '':
        text_surf = font.render(text, 1, pygame.Color('black'))
        # again, see how easy it is to center stuff using Rect's attributes like 'center'
        text_rect = text_surf.get_rect(center=rect.center)
        img.blit(text_surf, text_rect)
        return img
    
    # def set_flag(self, flag):
    #     # """Set the current flag ('X' or 'O') and update the button's image."""
    #         self.flag = flag
    #         text=self.flag
    #         self.image = self._create_image(CLICK_GRAY, None, text, self.rect)  # Recreate the surface with updated text

    def reset(self):
        self.image = self._create_image(CLICK_GRAY, None,'', pygame.Rect(0, 0, 120,120))
        self.org = self._create_image(REST_GRAY, None,'',pygame.Rect(0, 0, 120,120))
        self.hov = self._create_image(HOVER_GRAY, None,'', pygame.Rect(0, 0, 120,120))

    def update(self, events):
        # here we handle all the logic of the Button
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        global rest
        if rest==1:
            self.reset()
        # if the mouse in inside the Rect (again, see how the Rect class
        # does all the calculation for use), use the 'hov' image instead of 'org'
        self.image = self.hov if hit else self.org
        for event in events:
            # the Button checks for events itself.
            # if this Button is clicked, it runs the callback function
            if event.type == pygame.MOUSEBUTTONDOWN and hit:
                self.callback(self)
    def callback(self,x):
        self.image=self.press
        global flag
        global board
        global status
        
        if board[self.row][self.col]=='':
            if flag=='X':
                board[self.row][self.col]='X'
                self.text='X'
                flag='O'
            elif flag=='O':
                board[self.row][self.col]='O'
                self.text='O'
                flag='X'
        check_game_status(board)
        print(status)
        self.image = self._create_image(CLICK_GRAY, None, self.text, pygame.Rect(0, 0, 120,120))
        self.org = self._create_image(REST_GRAY, None, self.text,pygame.Rect(0, 0, 120,120))
        self.hov = self._create_image(HOVER_GRAY, None, self.text, pygame.Rect(0, 0, 120,120))

# we store all Sprites in a Group, so we can easily
# call the 'update' and 'draw' functions of the Buttons
# in the main loop
run = True
sprites = pygame.sprite.Group()
print(sprites)
sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(10, 10, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[0][0],
                   '',[0,0] 
                   ))#pygame.Color('black')

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(140, 10, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[0][1],
                   '',[0,1] 
                   ))#pygame.Color('black')

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(270, 10, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[0][2],
                   '',[0,2] 
                   ))#pygame.Color('black')

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(10, 140, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[1][0],
                   '',[1,0] 
                   ))#pygame.Color('black')

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(140, 140, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[1][1],
                   '',[1,1]
                   ))#pygame.Color('black')

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(270, 140, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[1][2],
                   '',[1,2] 
                   ))#pygame.Color('black')
 

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(10, 270, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[2][0],
                   '',[2,0] 
                   ))#pygame.Color('black')

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(140, 270, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[2][1],
                   '',[2,1]
                   ))#pygame.Color('black')

sprites.add(Button(pygame.Color(REST_GRAY),
                   pygame.Color(HOVER_GRAY),  # on hover color
                   pygame.Color(CLICK_GRAY),
                   # four parameters are position of rec (left,up,right,down) right and down cannot be zero
                   pygame.Rect(270, 270, 120, 120),
                   # //right these accor to display dimensions
                   # f1=pygame.font.SysFont('elephant',20)
                   lambda b: print(f"Button '{b.text}' was clicked"),
                   board[2][2],
                   '',[2,2] 
                   ))#pygame.Color('black')

def render_text(text):
    # Create the text surface
    text_surface = font.render(text, True, BLACK)    
    # Define the position for the text box (e.g., center of the screen)
    text_box_x = (WIDTH - BUTTON_HEIGHT) // 2-150
    text_box_y = (HEIGHT - BUTTON_HEIGHT) // 2+150
    text_box_width = 350
    text_box_height = 50    
    # Create a rectangle for the text box
    text_box_rect = pygame.Rect(text_box_x, text_box_y, text_box_width, text_box_height)    
    # Draw the text box background
    pygame.draw.rect(screen, REST_GRAY, text_box_rect)    
    # Center the text inside the text box
    text_rect = text_surface.get_rect(center=text_box_rect.center)    
    # Draw the text inside the box
    screen.blit(text_surface, text_rect)

def draw_reset_button():
    pygame.draw.rect(win, BUTTON_COLOR, reset_button_rect)
    button_text = BUTTON_FONT.render("Reset", True, BUTTON_TEXT_COLOR)
    button_text_rect = button_text.get_rect(center=reset_button_rect.center)
    win.blit(button_text, button_text_rect)

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if reset_button_rect.collidepoint(mouse_pos):
                board = [['' for _ in range(3)] for _ in range(3)]
                status='Ready'                
                rest=1

    # update all sprites
    # it now doesn't matter if we have one or 200 Buttons
    sprites.update(events)
    # clear the screen
    screen.fill(GREY)
    # draw all sprites/Buttons
    sprites.draw(screen)
    render_text(status)
    draw_reset_button()
    pygame.display.update()
    # limit framerate to 60 FPS
    clock.tick(20)