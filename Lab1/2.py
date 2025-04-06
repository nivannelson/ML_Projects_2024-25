'''
Develop a program to read the three sides of two triangles and
calculate the area of both. Define a function to read the three sides
and call it. Also, define a function to calculate the area. Print the total
area enclosed by both triangles and each triangle's contribution (%)
towards it.

Area=squareroot[ s(s-a)(s-b)(s-c)  ]

s= (a+b+c)/2

Datatype
Functions
Expressions
Built-in
functions

'''
import re

def Triinput(Tria):
    try:
        s1,s2,s3=re.split(r'[ ,]',Tria,maxsplit=3)
        Tridict={'a':s1,'b':s2,'c':s3}
        return Tridict  #store in dictionary
    except KeyboardInterrupt:
        print("Aborting...")
        exit(0)
    except Exception as e:
        print(e)
        main()

def TrigArea(Tria):
    a=float(Tria['a'])
    b=float(Tria['b'])
    c=float(Tria['c'])

    s= (a+b+c)/2
    Areaa=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return Areaa


import numpy as np
import math

def main():
    TriA={}
    TriB={}
    try:    
        inp=input("Enter length of 3 sides for triangle A comma/space separated a,b,c :")
        TriA=Triinput(inp)
        inp=input("Enter length of 3 sides for triangle B comma/space separated a,b,c :")
        TriB=Triinput(inp)
        print(f"Triangle A: {TriA['a']},{TriA['b']},{TriA['c']}")
        ar1=TrigArea(TriA)
        print(f"Area = {ar1}")
        print(f"Triangle B: {TriB['a']},{TriB['b']},{TriB['c']}")
        ar2=TrigArea(TriB)
        print(f"Area = {ar2}")
        total=ar1+ar2
        print(f"Total area enclosed by both triangles:{total}")
        if total!=0:
            print(f"A contributed {(ar1/total)*100}%")
            print(f"B contributed {(ar2/total)*100}%")
        else:
            print("Divide by zero error.Triangles dont exist")
            main()

    except KeyboardInterrupt:
        print("Aborting...")
        exit(0)
main()


'''
THINGS LEARNED
variable cant be initialized during printing?
datastructure dictionary handling

TODO
use more memory efficient data structures
better visualisation of results
adding unit conversion,decimal rounding

'''