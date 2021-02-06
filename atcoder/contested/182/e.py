import sys
input = sys.stdin.readline
H,W,N,M = list(map(int,input().split()))
grid = [[0] * (W) for _ in range(H)]
right_table=[[0] * W for _ in range(H)]
for _ in range(N):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    grid[a][b]=1
for _ in range(M):
    c,d=list(map(int,input().split()))
    c-=1
    d-=1
    grid[c][d]=-1
for h in range(H):
    flag = 0
    for w in range(W):
        if grid[h][w]==1:flag=1
        if grid[h][w]==-1:flag=0
        right_table[h][w]|=flag
    flag=0
    for w in reversed(range(W)):
        if grid[h][w]==1:flag=1
        if grid[h][w]==-1:flag=0
        right_table[h][w]|=flag
for w in range(W):
    flag=0
    for h in range(H):
        if grid[h][w]==1:flag=1
        if grid[h][w]==-1:flag=0
        right_table[h][w]|=flag
    flag=0 
    for h in reversed(range(H)):
        if grid[h][w]==1:flag=1
        if grid[h][w]==-1:flag=0
        right_table[h][w]|=flag
ans=0
for h in range(H):
    for w in range(W):
        if right_table[h][w] == 1:
            ans+=1

print(ans)