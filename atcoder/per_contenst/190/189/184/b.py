N,X=list(map(int,input().split()))
S=input().rstrip()
for s in S:
    if s=='x':
        X=max(0,X-1)
    else:
        X+=1
print(X)