# https://atcoder.jp/contests/abc007/tasks/abc007_3
H,W = list(map(int, input().split()))
sx,sy = list(map(lambda x : int(x)-1, input().split()))
gx,gy = list(map(lambda x : int(x)-1, input().split()))
grid = [list(input()) for _ in range(H)]
from collections import deque
dist = [[-1] * W for _ in range(H)]
dist[sx][sy] = 0
que = deque([[sx,sy]])
dx=[0,1,0,-1]
dy=[1,0,-1,0]
while len(que) > 0:
    h,w = que.popleft()
    for i in range(4):
        nh,nw = h+dx[i],w+dy[i]
        if not(0<=nh<H and 0<=nw<W):continue
        if dist[nh][nw] > -1 or grid[nh][nw] == "#":continue
        dist[nh][nw] = dist[h][w] + 1
        que.append([nh,nw])
print(dist[gx][gy])