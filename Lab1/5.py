'''
Develop a program to read a string and perform the following
operations:
• Print all possible substrings.
• Print all possible substrings of length K.
• Print all possible substrings of length K with N distinct
characters.
• Print substring(s) of length maximum length with N distinct
characters.
• Print all palindrome substrings.
Define function for each of the task.

Strings,
String
functions,
Slicing
'''
import numpy as np
unique=[]
def FindUni(substr,N=2):
    for i in range(len(substr)):
        if len(set(substr[i])) == N:
            unique.append(substr[i]) 
    return unique
         
def SubFindK(str,K):
    output=([str[i:i+K] for i in range(len(str)) if i+K<len(str)])
    return output 

def Subfind(str,length=None): #string "example" length is 7 cell 0-6
    output=set()
    N=4

    for i in range(len(str)):
        for j in range(i,len(str)+1):
            if length is None:
                output.add(str[i:j])
                continue
            else :
                for j in range(i,i+length+1):
                        output.add(str[i:j])
    output=list(output)
    return output

def Pald(str):
        pald=[]
        for i in range(len(str)):
            rev=str[i]
            if str[i]==rev[::-1]:
                pald.append(str[i])
        return pald


def main():
    strn=input("Enter a string: ")
    ch=input("""
1. Print all possible substrings.
2. Print all possible substrings of length K.
3. Print all possible substrings of length K with N distinct
characters.
4. Print substring(s) of length maximum length with N distinct
characters.
5. Print all palindrome substrings.
          
Type your choise(1-5):""")
    match(ch):
        case '1':
            print(Subfind(strn))
        case '2':
            print("type additional values")
            K=int(input("K: "))
            print(SubFindK(strn,K))
        case '3':
            print("type additional values")
            K=int(input("K: "))
            N=int(input("N: "))
            str=SubFindK(strn,K)
            print(FindUni(str,N))
        case '4':
            print("type additional values")
            N=int(input("N: "))
            length=int(input("Length: "))
            str=Subfind(strn,length)
            print(FindUni(str,N))
        case '5':
            str=Subfind(strn)
            print(Pald(str))


main()


'''
THINGS LEARNING
unidecode,textwrap,fuzzywuzzy,nltk,strsimile packages
Python has a default recursion depth limit of 1000
List comprehension
TODO
improve performace for finding distinct uniques using Hashmaps
'''