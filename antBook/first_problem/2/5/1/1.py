import sys

sys.setrecursionlimit(10**9)

N=int(input())
edges = [[] for _ in range(N)]

for _ in range(N-1):
    u,v,w = list(map(int, input().split()))
    u-=1
    v-=1
    edges[v].append([u,w])
    edges[u].append([v,w])

ans = [-1] * N

def dfs(t, color):
    for u, w in edges[t]:
        if ans[u] != -1:continue
        next_color = color if w%2 == 0 else abs(color - 1)
        ans[u] = next_color
        dfs(u, next_color)
ans[0]=0
dfs(0, 0)
print(*ans, sep='\n')