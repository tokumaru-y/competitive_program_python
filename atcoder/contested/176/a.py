N,X,T=list(map(int,input().split()))
d = N//X + 1 if N%X!=0 else N//X
print(T*d)