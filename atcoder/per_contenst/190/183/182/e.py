H,W,N,M=list(map(int,input().split()))
grid=[[0]*W for _ in range(H)]
for _ in range(N):
    a,b=list(map(int,input().split()))
    a,b=a-1,b-1
    grid[a][b]=1
for _ in range(M):
    c,d=list(map(int,input().split()))
    c,d=c-1,d-1
    grid[c][d]="#"
lignts=[[0]*W for _ in range(H)]
for h in range(H):
    lig=0
    for w in range(W):
        if grid[h][w]=="#":lig=0
        if grid[h][w]==1:lig=1
        lignts[h][w]+=lig
    lig=0
    for w in reversed(range(W)):
        if grid[h][w]=="#":lig=0
        if grid[h][w]==1:lig=1
        lignts[h][w]+=lig
for w in range(W):
    lig=0
    for h in range(H):
        if grid[h][w]=='#':lig=0
        if grid[h][w]==1:lig=1
        lignts[h][w]+=lig
    lig=0
    for h in reversed(range(H)):
        if grid[h][w]=='#':lig=0
        if grid[h][w]==1:lig=1
        lignts[h][w]+=lig
ans=0
for h in range(H):
    for w in range(W):
        if lignts[h][w]>0:ans+=1
print(ans)