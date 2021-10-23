# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
import sys
sys.setrecursionlimit(10**9)
dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]
def dfs(graph, x, y, seen,lh,lw):
    seen[x][y]=True
    for i in range(8):
        nx,ny = x+dx[i], y+dy[i]
        if not(0<=nx<lh and 0<=ny<lw) or graph[nx][ny] == 0:continue
        if seen[nx][ny]:continue
        dfs(graph, nx,ny,seen, lh, lw)

while True:
    W,H=list(map(int, input().split()))
    if H+W==0:break
    graph = []
    for _ in range(H):
        graph.append(list(map(int, input().split())))
    seen = [[False] * W for _ in range(H)]
    cnt = 0
    for h in range(H):
        for w in range(W):
            if seen[h][w] or graph[h][w]==0:continue
            dfs(graph,h,w,seen,H,W)
            cnt += 1
    print(cnt)