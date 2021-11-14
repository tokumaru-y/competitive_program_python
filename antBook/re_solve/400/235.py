# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c
from collections import deque
H,W,K=list(map(int, input().split()))
grid = [input() for _ in range(H)]
ans = [[-1] * W for _ in range(H)]
num = 0
for w in range(W):
    is_existed = False
    for h in range(H):
        if grid[h][w] == "#":is_existed=True
    if is_existed:
        for h in range(H):
            if grid[h][w] == "#":num += 1
            ans[h][w] = num
        for h in reversed(range(1,H)):
            if grid[h-1][w] == "#":continue
            ans[h-1][w] = ans[h][w]
    else:
        if w == 0:continue
        for h in range(H):
            if grid[h][w] == "#":continue
            ans[h][w] = ans[h][w-1]
for w in reversed(range(1,W)):
    for h in range(H):
        if ans[h][w-1] > -1:continue
        ans[h][w-1] = ans[h][w]

for a in ans:
    print(*a,sep=" ")