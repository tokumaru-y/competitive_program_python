# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
import copy
H,W=list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for bit in range(1<<H):
    tmp_grid = copy.deepcopy(grid)
    for i in range(H):
        if not (bit & 1<<i):continue
        for j in range(W):
            tmp_grid[i][j] = 1 - tmp_grid[i][j]
    tmp = 0
    for j in range(W):
        num = 0
        for i in range(H):
            if tmp_grid[i][j] == 0:num += 1
        tmp += max(num, H-num)
    ans = max(ans, tmp)
print(ans)