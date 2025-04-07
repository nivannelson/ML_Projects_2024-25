# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T=int(input())
Slist=[]
for i in range(T):
    Slist.append(input())
for pattern in Slist:
  try:
    re.compile(pattern)
    print("True")
  except re.error:
    print("False")