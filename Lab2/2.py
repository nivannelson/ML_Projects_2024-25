'''
Write a program to read a string containing numbers separated by a
space and convert it as a list of integers. Perform the following
operations on it.
1. Rotate elements in a list by 'k' position to the right
2. Convert the list into a tuple using list comprehension
3. Remove all duplicates from the tuple and convert them
into a list again.
4. Create another list by putting the results of the evaluation
of the function f(x) = x2 – x with each element in the final list
5. After sorting them individually, merge the two lists to
create a single sorted list.

List, tuple,
set, list
comprehen
sion
'''
def lstrot(lis,k=None):
    temp=[]
    temp=lis.copy()
    l=len(lis)
    rot=0
    for i in range(l):
        if k+i>=l:
            temp[rot]=lis[i]
            # print(f"T{rot}<--{i}")
            # print(f"lis={lis}")
            # print(f"temp={temp}")
            rot+=1
        else:
            temp[k+i]=lis[i]
            # print(f"{k+i}<--{i}")
            # print(f"lis={lis}")
            # print(f"temp={temp}")
    return temp

def tupconv(ls,ch,k=2):
    tflag=0
    match(ch): 
        case '1':
            k=int(input("input K:"))
            return lstrot(ls,k)
        case '2':
            ls=tuple(ls)
            return ls
        case '3':
            ls=set(ls)
            ls=list(ls)
            return ls
        case '4':
            newlist=[(lambda x:x**2 - x)(x) for x in ls]
            print(f"f(x) = x2 – x: {newlist}")
            return ls
        case '5':
            ls=sorted(ls)
            newlist=[(lambda x:x**2 - x)(x) for x in ls]
            newlist=sorted(newlist)
            print(f"new{newlist}")
            ls.extend(newlist)
            return ls
        case '' | _:
            for ch in range(1,6):
                ls=tupconv(ls,str(ch))
                print(f"for {ch}=={ls}")
            return ls

import re
def main():
    intlist=[]
    string=input("Enter list of integers separated by spaces")
    ch=input("""
1. Rotate elements in a list by 'k' position to the right
2. Convert the list into a tuple using list comprehension
3. Remove all duplicates from the tuple and convert them
into a list again.
4. Create another list by putting the results of the evaluation
of the function f(x) = x2 - x with each element in the final list
5. After sorting them individually, merge the two lists to
create a single sorted list.
            (1-5) or leave blank to do all:
                 """)
    intlist=re.split(r'[ ]',string)
    intlist=list(map(int,intlist))
    intlist=tupconv(intlist,ch)
    print(f"final list: {intlist}")
main()


'''
THINGS LEARNED
assigning list to another doesnt copy the contents but point to memory location 

TODO
Require resolution for:
    question logic is not fully understood
    questionable requirement for list comprehension.
'''