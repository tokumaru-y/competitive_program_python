# https://atcoder.jp/contests/arc031/tasks/arc031_2
grid = []
for i in range(10):
    inp = list(input())
    grid.append(inp)
tmp_grid = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
import sys
import copy
sys.setrecursionlimit(10**9)
seen = [[False] * 10 for _ in range(10)]
def dfs(x, y):
    seen[x][y]=True
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if not (0<=nx<10 and 0<=ny<10):continue
        if seen[nx][ny] or tmp_grid[nx][ny]=="x":continue
        dfs(nx,ny)
for h in range(10):
    for w in range(10):
        seen = [[False] * 10 for _ in range(10)]
        tmp_grid = copy.deepcopy(grid)
        tmp_grid[h][w]= "o"
        cnt = 0
        for i in range(10):
            for j in range(10):
                if seen[i][j] or grid[i][j] == "x":continue
                dfs(i,j)
                cnt+= 1
        if cnt == 1:
            print("YES")
            exit()
print("NO")
