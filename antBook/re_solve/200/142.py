# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
from copy import deepcopy
R,C=list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(R)]
ans = 0
for bit in range(1<<R):
    tmp_grid = deepcopy(grid)
    cnt_table = [0] * C
    for i in range(R):
        if bit & (1<<i):
            for j in range(C):
                tmp_grid[i][j] = 1-grid[i][j]
    for i in range(R):
        for j in range(C):
            cnt_table[j]+=tmp_grid[i][j]
    tmp_ans = 0
    for j in range(C):tmp_ans += max(cnt_table[j], R-cnt_table[j])
    ans = max(ans, tmp_ans)
print(ans)
