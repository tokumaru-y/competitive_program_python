import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int,input().split()))
colors = [-1]*N
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
def dfs(t,c):
    for nt in graph[t]:
        if colors[nt] > -1:continue
        nc = abs(c-1)
        colors[nt]=nc
        dfs(nt, nc)
colors[0]=0
dfs(0,0)
print(sum(colors)+1)