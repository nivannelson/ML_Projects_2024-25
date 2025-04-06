'''
Develop a program to perform the following task:
a. Define a function to check whether a number is happy or not.
b. Define a function to print all happy numbers within a range.
c. Define a function to print first N happy numbers.
A happy number is a number defined by the following process:
• Starting with any positive integer, replace the number with the
sum of the squares of its digits.
• Repeat the process until the number equals 1 (where it will
stay), or it loops endlessly in a cycle which does not include 1.
• Those numbers for which this process ends in 1 are happy.
Note: if a number is not being happy after 100 iterations, consider it
sad.

Loops – for,
while
Nested
loops
'''

def isHpy(num):
    cnt=1
    while int(num)!=1 and cnt<100:
        temp=str(int(num))
        sqsum=0
        l=len(temp)
        # print(f"{temp} and {l}")
        for x in range(0,l):
            sqsum+=math.pow(int(temp[x]),2)  #sum of digits squares
            # print(f"test{sqsum}")
            x+=1
        num=sqsum
        cnt+=1
    if num==1:
        return ')'
    else:
        return 'O'
    #function to check whether a number is happy or not.

def FindHpy(fir,end):
    #function to print all happy numbers within a range.
    hpylist=[]
    for i in range(fir,end+1):
        if isHpy(i)==')':
            hpylist.append(i)
    return hpylist
def FirstHpy(N):
    #function to print first N happy numbers.
    firsthpy=[]
    cnt=0
    while cnt<=N:
        if isHpy(cnt)==')':
            firsthpy.append(cnt)
        cnt+=1    
    return firsthpy

import random
import math

def main():
    try:
        num=input("Enter a positive integer or simply press enter for random")
        if num == "":
            num= random.randrange(0,10000)
        print(f"{num} was choosen.")     #replace the number with the sum of the squares of its digits
        print(":O --> sad    :) --> happy")
        print(f"{num} is :{isHpy(num)}")
        ch=input("""type 1 to find :) numbers in a range\n
type 2 to find first :) till N numbers.Type 12 for both or press enter to exit\n          :""")
        if ch=='':
            exit(0)
        if int(ch)==1 or int(ch)==12:
            fir=int(input("Range start at:"))
            end=int(input("Range end at:"))
            print(f"{fir},{end} range: {FindHpy(fir,end)}")
        if int(ch)==2 or int(ch)==12:
            N=input("Enter a positive integer(N) or press enter for random")
            if N == "":
                N= random.randrange(0,10000)
                print(f"{N} was choosen.")
            print(f":) till {N}: {FirstHpy(N)}")

                
    except KeyboardInterrupt:
        print("Aborting...")
        exit(0)
    except Exception as e:
        print(e)
        main()

main()

'''
THINGS LEARNED
str() can convert integer to string
exponents in math lib
range return False if == last
TODO

'''