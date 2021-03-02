S=input().rstrip()
scnt=S.count('R')
if S[1]=='S':
    print(0 if scnt==0 else 1)
else:
    print(scnt)