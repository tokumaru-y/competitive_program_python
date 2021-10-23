# https://atcoder.jp/contests/arc037/tasks/arc037_b
N,M=list(map(int, input().split()))
UV=[list(map(int,input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]
for u,v in UV:
    u,v=u-1,v-1
    graph[u].append(v)
    graph[v].append(u)
from collections import deque
pos = -1
seen = [False] * N
finish = [False] * N    
history = deque([])
def dfs_cycle(v, p):
    global pos
    seen[v] = True
    history.append(v)
    for nv in graph[v]:
        if nv == p:continue
        if finish[nv]:continue
        # サイクル検出
        if seen[nv] and not finish[nv]:
            pos = nv
            return
        dfs_cycle(nv, v)
        if pos != -1:
            return
    history.pop()
    finish[v]=True
ans = 0
for i in range(N):
    if seen[i]:continue
    pos = -1
    dfs_cycle(i,-1)
    if pos == -1:ans += 1
print(ans)