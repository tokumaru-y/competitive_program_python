import sys

sys.setrecursionlimit(10**5)
B=[list(map(int, input().split())) for _ in range(2)]
C=[list(map(int, input().split())) for _ in range(3)]
sum_point = sum(map(sum, B))
sum_point+= sum(map(sum, C))
grid = [[0] * 3 for _ in range(3)]
def calc(grid):
    res = 0
    for i in range(2):
        for j in range(3):
            if grid[i][j] == grid[i+1][j]:res+=B[i][j]
    for i in range(3):
        for j in range(2):
            if grid[i][j] == grid[i][j+1]:res+=C[i][j]
    return res

def dfs(grid,time):
    if time == 9:
        return calc(grid)
    res = float("-inf") if time%2==0 else float("inf")
    value = 1 if time%2==0 else -1
    minmax = max if time%2==0 else min
    for i in range(3):
        for j in range(3):
            if grid[i][j] != 0:continue
            grid[i][j] = value
            res = minmax(res, dfs(grid, time+1))
            grid[i][j] = 0
    return res
ans = dfs(grid, 0)
print(ans, sum_point-ans, sep="\n")
