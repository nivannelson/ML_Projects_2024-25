def merge_the_tools(string, k):
    # your code goes here
    t1=[string[i:i+k] for i in range(0,len(string),k)]
    u1 = [set(t1[i]) for i in range(0,len(t1))]
    for i in range (0,len(u1)):
      temp=''.join(u1[i])
      u1[i]=temp
      print(u1[i])


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)