import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]
for u,v in UV:
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)
MOD = 998244353
pos = -1
seen = [False] * N
finish = [False] * N
max_cnt = 0 
def dfs_cycle(v, p):
    global pos
    global max_cnt
    tmp_cnt = 0
    seen[v] = True
    for nv in graph[v]:
        if nv == p:continue
        if finish[nv]:continue
        # サイクル検出
        if seen[nv] and not finish[nv]:
            pos = nv
            return
        tmp_cnt += 1
        dfs_cycle(nv, v)
        if pos != -1:
            return
    finish[v]=True
    max_cnt = max(max_cnt , tmp_cnt)
ans = 1
for i in range(N):
    if seen[i]:continue
    pos=-1
    max_cnt = 0
    dfs_cycle(i, -1)
    if pos != -1:
        ans *= 2
        ans %= MOD
    else:
        ans *= max_cnt
        ans %= MOD
print(ans if ans > 1 else 0)