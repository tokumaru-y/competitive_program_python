N=int(input())
AB=[list(map(int,input().split())) for _ in range(N)]
X=[]
sa=0
for a,b in AB:
    X.append([a,b,a+b])
    sa+=a
X.sort(lambda x : -x[2])
Takahashi=0
for i in range(N):
    a,b,c=X[i]
    