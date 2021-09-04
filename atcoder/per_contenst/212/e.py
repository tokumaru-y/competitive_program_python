from collections import deque
N=int(input())
K=int(input())
grid = [list(input()) for _ in range(N)]
ans = 0
di = [[0,1],[0,-1],[1,0],[-1,0]]
used_grid = {}
def dfs(cnt):
    str_grid= ""
    for i in range(N):
        str_grid += "".join(grid[i])
    if str_grid in used_grid:
        return
    used_grid[str_grid] = 1
    if cnt == 0:
        global ans
        ans += 1
        return
    q = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                flag = False
                for x,y in di:
                    nx=x+i
                    ny=y+j
                    if (0<=nx<=N-1 and 0<=ny<=N-1) and grid[nx][ny] == "@":
                        flag = True
                if flag:q.append([i,j])
    for s, t in q:
        grid[s][t] = "@"
        dfs(cnt-1) 
        grid[s][t] = "."
for i in range(N):
    for j in range(N):
        if grid[i][j] == ".":
            grid[i][j] = "@"
            dfs(K-1)
            grid[i][j] = "."
print(ans)