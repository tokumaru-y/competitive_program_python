# https://atcoder.jp/contests/abc226/tasks/abc226_e
import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int, input().split()))
UV=[list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]
for u,v in UV:
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)
MOD = 998244353
seen = [False] * N
top, edge = 0,0
def dfs(v):
    seen[v] = True
    global top
    global edge
    top += 1
    edge += len(graph[v])
    for nv in graph[v]:
        if not seen[nv]:dfs(nv)
cnt = 0
for i in range(N):
    if seen[i]:continue
    top = 0
    edge = 0
    dfs(i)
    if top * 2 == edge:cnt += 1
    else:
        print(0)
        exit()
print((2 ** cnt) % MOD)