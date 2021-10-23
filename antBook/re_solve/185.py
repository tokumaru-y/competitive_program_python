# https://atcoder.jp/contests/atc001/tasks/dfs_a
H,W=list(map(int, input().split()))
grid = []
sx,sy = 0,0
gx,gy = 0,0
for i in range(H):
    inp = list(input())
    for j in range(W):
        if inp[j] == "s":
            sx,sy = i,j
        if inp[j] == "g":
            gx,gy = i,j
    grid.append(inp)
import sys
sys.setrecursionlimit(10**9)
seen = [[False] * W for _ in range(H)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs(x,y):
    seen[x][y]=True
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if not (0<=nx<H and 0<=ny<W):continue
        if seen[nx][ny] or grid[nx][ny] == "#":continue
        dfs(nx,ny)
dfs(sx,sy)
print("Yes" if seen[gx][gy] else "No")