# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__ =='__main__':
    data=[]
    row,column=map(int,input().split())
    for i in range(row):
        data.append(list(map(int,input().split())))
    matrix=np.array(data)
    print(np.transpose(matrix))
    print(matrix.flatten())