import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int, input().split()))
edges = [[] * N for _ in range(N)]

for _ in range(M):
    a,b = list(map(int,input().split()))
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)

graph = [-1] * N
graph[0]=0
def dfs(top, color):
    next_color = abs(color -1)
    for e in edges[top]:
        if graph[e] != -1:
            if graph[e] == color:
                return False
            continue
        graph[e]=next_color
        if not dfs(e, next_color):
            return False
    return True
is_bipartite_graph = dfs(0,0)
if is_bipartite_graph:
    black = graph.count(1)
    white = graph.count(0)
    ans = black*white - M
else:
    ans = (N*(N-1))//2 - M
print(ans)