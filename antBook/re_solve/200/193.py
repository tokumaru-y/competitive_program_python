# https://atcoder.jp/contests/arc005/tasks/arc005_3
H,W=list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j] == "s":
            sh,sw = i,j
        elif grid[i][j] == "g":
            gh,gw = i,j
from collections import deque
dist = [[-1] * W for _ in range(H)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dist[sh][sw] = 0
que = deque([[sh,sw]])
while len(que) > 0:
    h,w = que.popleft()
    for i in range(4):
        nh,nw = h+dx[i], w+dy[i]
        if not(0<=nh<H and 0<=nw<W):continue
        if dist[nh][nw] > -1:continue
        if grid[nh][nw] == "#":
            if dist[h][w] == 2:continue
            que.append([nh,nw])
            dist[nh][nw] = dist[h][w] + 1
        else:
            que.appendleft([nh,nw])
            dist[nh][nw] = dist[h][w]
print("YES" if dist[gh][gw] >= 0 else "NO")