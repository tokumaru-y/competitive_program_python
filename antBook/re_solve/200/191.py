# https://atcoder.jp/contests/abc088/tasks/abc088_d
H,W=list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
black_cnt = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":black_cnt+=1
from collections import deque
dist = [[-1] * W for _ in range(H)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dist[0][0]=0
que = deque([[0,0]])
while len(que) > 0:
    h,w = que.popleft()
    for i in range(4):
        nh,nw = h+dx[i],w+dy[i]
        if not(0<=nh<H and 0<=nw<W):continue
        if grid[nh][nw] == "#" or dist[nh][nw] > -1:continue
        dist[nh][nw] = dist[h][w] + 1
        que.append([nh,nw])
if dist[H-1][W-1] == -1:
    ans = -1
else:
    ans = H * W - black_cnt - dist[H-1][W-1] - 1
print(ans)