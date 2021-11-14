# https://atcoder.jp/contests/agc043/tasks/agc043_a
import sys
sys.setrecursionlimit(10**9)
from collections import deque
H,W=list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
ans = [[float("inf")] * W for _ in range(H)]
ans[0][0] = 0 if grid[0][0] == "." else 1
q = deque([[0,0,True if grid[0][0] == "#" else False]])
while len(q):
    h,w,pre_removed = q.popleft()
    cnt = ans[h][w]
    for x,y in zip([1,0],[0,1]):
        nh,nw=h+x,w+y
        if not(0<=nh<H and 0<=nw<W):continue
        if grid[nh][nw] == "#":
            next_cnt = cnt if pre_removed else cnt+1
            if ans[nh][nw] <= next_cnt:continue
            ans[nh][nw] = next_cnt
            q.append([nh,nw,True])
        else:
            if ans[nh][nw] <= cnt:continue
            ans[nh][nw] = cnt
            q.append([nh,nw,False])
print(ans[H-1][W-1])