

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


str="examplexxe"
str=Subfind(str)
print(Pald(str))