#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if math.fmod(n,2)==1:
        print("Weird")
    elif n in range(2,5) or n==2:
        print("Not Weird")
    elif n in range(6,20) or n==6 or n==20:
        print("Weird")
    elif n>20:
        print("Not Weird") 
