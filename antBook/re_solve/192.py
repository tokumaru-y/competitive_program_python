# https://atcoder.jp/contests/agc033/tasks/agc033_a
H,W=list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
from collections import deque
dist = [[-1] * W for _ in range(H)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
black = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            black.append([i,j])
que = deque([black])
ans = 0
while len(que) > 0:
    black_list = que.popleft()
    is_done = False
    next_list = []
    for h,w in black_list:
        for i in range(4):
            nh,nw = h+dx[i],w+dy[i]
            if not(0<=nh<H and 0<=nw<W):continue
            if grid[nh][nw] == "#":continue
            grid[nh][nw] = "#"
            is_done = True
            next_list.append([nh,nw])
    if len(next_list) > 0:
        que.append(next_list)
    if is_done:ans += 1
print(ans)