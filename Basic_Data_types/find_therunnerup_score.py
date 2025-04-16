if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    highest = float('-inf')
    runnerup = float('-inf')
    for score in arr:
        if score>highest:
            highest=score
    for score in arr:
        if score>runnerup and score!=highest:
            runnerup=score

    print(runnerup)