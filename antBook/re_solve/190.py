# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
H,W,N=list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            sx,sy = i,j
from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]
ans = 0
for cheese_num in range(1,N+1):
    dist = [[-1] * W for _ in range(H)]
    dist[sx][sy]=0
    que = deque([[sx,sy]])
    while len(que) > 0:
        h,w = que.popleft()
        for i in range(4):
            nh,nw = h+dx[i], w+dy[i]
            if not (0<=nh<H and 0<=nw<W):continue
            if grid[nh][nw] == "X" or dist[nh][nw] > -1:continue
            if grid[nh][nw] == str(cheese_num):
                ans += dist[h][w] + 1
                sx,sy = nh,nw
                que = []
                break
            dist[nh][nw] = dist[h][w] + 1
            que.append([nh,nw])
print(ans)
