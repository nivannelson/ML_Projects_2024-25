'''
Suppose a newly born pair of rabbits, one male and one female, are
put in a field. Rabbits can mate at the age of one month so that at the
end of its second month, a female has produced another pair of
rabbits. Suppose that our rabbits never die and that the female always
produces one new pair every month from the second month.
Develop a program to show a table containing the number of pairs of
rabbits in the first N months.

Critical
thinking,
Loops,
formatted
io.
'''
'''
M-male -1 month
F-female -1 month
B-baby -1 month

when take each cycle to be 1 month.
lets set flags to the rabbits
M=0-young,1-ready
F=0-young,1-ready,2-pregnant

it takes 1 cycle for

if M=0 to be 1 but it stays 1 for the latter cycles.
if F=0 to be 1 but after it is 2 and take one more cycle to be 1.

'''




import pandas as pd
global Flist
Flist=[]


def SetF(flag):
    if flag==0:
        flag=2
    elif flag==1:
        flag=2
    elif flag==2:
        Flist.append(0)
    return flag

def Cycle():
    for i in range(len(Flist)):
        Flist[i]=SetF(Flist[i])


def main():
    table=[]
    Flist.append(0)
    print("how many loops")
    month=int(input())

    for i in range(month+1):
        table.append([i,len(Flist)])
        # print(i)
        # print(Flist)
        Cycle()
    df = pd.DataFrame(table, columns=["Month","Pair(s)"])
    print(df.to_string(index=False))

main()