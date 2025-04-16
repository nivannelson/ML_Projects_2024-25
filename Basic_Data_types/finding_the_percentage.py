if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for marks in student_marks[query_name]:
        total+=marks
    print(f"{total/3:.2f}")