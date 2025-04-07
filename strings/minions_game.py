def minion_game(string):
    Stuart=0
    Kevin=0
    length=len(string)
    for i in range(length):
      score=length-i
      if string[i] in ['A','E','I','O','U']:
        Kevin+=score
      else:
        Stuart+=score
    if Kevin==Stuart:
        print("Draw")
    elif Kevin>Stuart:
        print(f"Kevin {Kevin}")
    elif Stuart>Kevin:
        print(f"Stuart {Stuart}") 

if __name__ == '__main__':
    s = input()
    minion_game(s)