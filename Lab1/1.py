'''
Develop a program to read a four-digit number and find its
a. Sum of digits
b. Reverse
c. Difference between the product of digits at the odd position
and the product of digits at the even position.
Example:
Input
234
Output
10 (1+2+3+4)
4321
-5(1*3 - 2*4)

input ()
Strings
Arithmetic
operators

'''
def Sum(inpnum):
    print("Sum of digits = (",end="")
    l=len(inpnum)
    cnt=0
    answer=0
    while True:
        num=int(inpnum[cnt])
        print(num,end="")
        answer+=num
        cnt+=1
        if cnt>=l:
            print(")",end="")
            break
        print("+",end="")
    print(f": {answer}")
def Rev(inpnum):
    print("Reverse =",end="")
    print(inpnum[::-1])

def Diff(inpnum):
    cnt=1
    l=len(inpnum)
    p1=1
    print("Product of digits at the odd position = (",end="")
    while True:
        #Cal product of digits in odd
        num=int(inpnum[cnt])
        print(num,end="")
        p1*=num
        cnt+=2
        if cnt>=l:
            print(")",end="")
            break
        print("x",end="")
    print(f": {p1}")
    cnt=0
    p2=1
    print("Product of digits at the even position = (",end="")
    while True:
        #Cal product of digits in even
        num=int(inpnum[cnt])
        print(num,end="")
        p2*=num
        cnt+=2
        if cnt>=l:
            print(")",end="")
            break
        print("x",end="")
    print(f": {p2}")
    print(f"Difference {p1}-{p2}= {p1-p2}")



import numpy as np
import os
import time
def main():
    try:
        
        inpnum=input("Enter a number:")
        print(type(inpnum))
        while True:
            choise=input("""a. Sum of digits\n
b. Reverse\n
c. Difference between the product of digits at the odd position\n
and the product of digits at the even position.
d. All of the above
type[a/b/c/d]:""")
            match(choise.lower()):
                case "a":
                    Sum(inpnum)
                    break
                case "b":
                    Rev(inpnum)
                    break
                case "c":                    
                    Diff(inpnum)
                    break
                case "d":
                    Sum(inpnum)
                    time.sleep(0.2)
                    Rev(inpnum)
                    time.sleep(0.2)
                    Diff(inpnum)
                    break
                case default:
                    print(f"user typed \"{choise}\" is not one of the options.Try Again")
                    time.sleep(1)
                    os.system("cls")

    except KeyboardInterrupt:
        print("Aborting...")
        exit(0)
    except Exception as e:
        print()
        os.system("cls")
        print(e)
        main()

        


main()


'''
THINGS LEARNED
\033[A dont work for Windows
match case could replace switch() in C++
print by default end="\n"
python no support Goto
cls for windows clear for Linux,Mac
[::-1] in numpy reverses array

TODO
sleep fuction of time slows down execution so larger processes must be multi threaded.
minimise while and if statements
'''