H,W=list(map(int,input().split()))
grid = [input().rstrip() for _ in range(H)]
eh=-1
ew=-1
for h in range(H):
    for w in range(W):
        if grid[h][w]=="#":
            eh=h
            ew=w
            break
    if eh!=-1 and ew !=-1:break
cnt=[[False] * W for _ in range(H)]
cnt[eh][ew]=True
dd = [[1,0],[0,1]]
total=0
def dfs(x,y,dirx):
    global total
    for d in dd:
        nh=x+d[0]
        nw=y+d[1]
        if not(0<=nh<=H-1 and 0<=nw<=W-1):continue
        if grid[nh][nw]=='#' and d != dirx:
            total+=1
        if grid[nh][nw]=="#" and not cnt[nh][nw]:
            cnt[nh][nw]=True
            dfs(x,y,d)
dfs(eh,ew,[0,0])
print(total)