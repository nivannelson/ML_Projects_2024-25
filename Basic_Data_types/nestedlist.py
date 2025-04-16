if __name__ == '__main__':
    record=[]
    lowest=float('+inf')
    secondlowest=float('+inf')
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
    record.sort(key=lambda x: x[0])    
    for item in record:
        if item[1]<lowest:
            lowest=item[1]
    for item in record:
        if item[1]<secondlowest and item[1]!=lowest:
            secondlowest=item[1]
    for item in record:
        if item[1]==secondlowest:
            print(item[0])