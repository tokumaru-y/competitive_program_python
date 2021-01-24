n=int(input())
grids=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
memos=[[[1,0,0],[0,1,0],[0,0,0]]for _ in range(m+1)]
def cal1(ind,clockwise):
    origin=memos[ind-1]
    tmp=[[0,0,0] for _ in range(3)]
    if clockwise:
        t=[[0,1,0],[-1,0,0],[0,0,0]]
    else:
        t=[[0,-1,0],[1,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                tmp[i][j]+=t[i][k]*origin[j][k]

    memos[ind]=tmp
def cal2(ind,p,x):
    origin=memos[ind-1]
    tmp=[[0,0,0]for _ in range(3)]
    if x:
        t=[[-1,0,2*p],[0,1,0],[0,0,0]]
    else:
        t=[[1,0,0],[0,-1,2*p],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                tmp[i][j]+=t[i][k]*origin[j][k]
    memos[ind]=tmp

for ind in range(m):
    a=list(map(int,input().split()))
    if a[0]==1:
        cal1(ind+1,True)
    elif a[0]==2:
        cal1(ind+1,False)
    elif a[0]==3:
        cal2(ind+1,a[1],True)
    elif a[0]==4:
        cal2(ind+1,a[1],False)

q=int(input())
for _ in range(q):
    a,b=list(map(int,input().split()))
    b-=1
    target=grids[b]
    x=target[0]*memos[a][0][0]+target[1]*memos[a][0][1]
    y=target[0]*memos[a][1][0]+target[1]*memos[a][1][1]
    print(x,y)