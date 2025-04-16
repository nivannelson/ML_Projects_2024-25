# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

if __name__=='__main__':
    data=[]
    row1,row2,column=map(int,input().split())
    for i in range(row1):
        data.append(list(map(int,input().split())))
    matrix1=np.array(data)
    data=[]
    for i in range(row2):
        data.append(list(map(int,input().split())))
    matrix2=np.array(data)
    print(np.concatenate((matrix1,matrix2),axis=0))

