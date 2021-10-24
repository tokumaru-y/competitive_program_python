import sys
sys.setrecursionlimit(10**5)
N=int(input())
ans = [-1] * N
graph = [[] for _ in range(N)]
for _ in range(N-1):
    u,v,w=list(map(int, input().split()))
    u-=1
    v-=1
    graph[u].append([v,w])
    graph[v].append([u,w])
def dfs(x, color):
    ans[x] = color
    for v, l in graph[x]:
        if ans[v] != -1:continue
        if l%2==0:
            dfs(v, color)
        else:
            dfs(v, abs(color-1))
dfs(0,0)
print(*ans, sep="\n")