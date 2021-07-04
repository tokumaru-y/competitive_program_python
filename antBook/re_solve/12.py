import sys
sys.setrecursionlimit(10**5)
N,M=list(map(int, input().split()))
graph=[[] for _ in range(N)]
type = [-1] * N
for _ in range(M):
    a,b = list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
def dfs(x, t):
    type[x]=t
    for v in graph[x]:
        if type[v] == t:return False
        if type[v] != -1:continue
        if not dfs(v,abs(t-1)): return False
    return True
is_bin_graph = dfs(0,0)
if is_bin_graph:
    b,w = 0,0
    for i in range(N):
        if type[i] == 0:
            b+=1
        else:
            w += 1
    ans = b * w - M
else:
    ans = N*(N-1)//2 - M
print(ans)