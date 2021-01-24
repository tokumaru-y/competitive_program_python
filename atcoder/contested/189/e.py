n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
do=[list(map(int,input().split())) for _ in range(m)]
memos=[[[1,0,0],[0,1,0],[0,0,1]]]
def cal1(i,clockwise):
    origin=memos[i]
    tmp=[[0,0,0] for _ in range(3)]
    if clockwise:
        t=[
            [0,1,0],
            [-1,0,0],
            [0,0,1]
        ]
    else:
        t=[
            [0,-1,0],
            [1,0,0],
            [0,0,1]
        ]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                tmp[i][j]+=t[i][k]*origin[k][j]
    memos.append(tmp)

def cal2(i,p,is_x):
    origin=memos[i]
    tmp=[[0,0,0] for _ in range(3)]
    if is_x:
        t=[
            [-1,0,2*p],
            [0,1,0],
            [0,0,1]
        ]
    else:
        t=[
            [1,0,0],
            [0,-1,2*p],
            [0,0,1]
        ]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                tmp[i][j]+=t[i][k]*origin[k][j]
    memos.append(tmp)
for i,d in enumerate(do):
    if d[0]==1:
        cal1(i,True)
    elif d[0]==2:
        cal1(i,False)
    elif d[0]==3:
        cal2(i,d[1],True)
    elif d[0]==4:
        cal2(i,d[1],False)

q=int(input())
for _ in range(q):
    a,b=list(map(int,input().split()))
    b-=1
    x,y=xy[b]
    print(x*memos[a][0][0]+y*memos[a][0][1]+memos[a][0][2],x*memos[a][1][0]+y*memos[a][1][1]+memos[a][1][2])
