N=int(input())
AB=[list(map(int,input().split())) for _ in range(N)]
X=[]
s=0
for a,b in AB:
    X.append([a,b,2*a+b])
    s += -a
X=sorted(X, key = lambda x : -x[2])
for i in range(N):
    a,b,c=X[i]
    s+=c
    if s > 0:
        print(i+1)
        exit()