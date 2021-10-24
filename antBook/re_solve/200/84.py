import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
is_bin_graph = True
colors = [-1] * N
def dfs(t, c):
    global is_bin_graph
    nc = abs(c-1)
    for nt in graph[t]:
        if colors[nt] == c:
            is_bin_graph=False
            break
        elif colors[nt] > -1:continue
        colors[nt]=nc
        dfs(nt, nc)
colors[0]=0
dfs(0,0)
if is_bin_graph:
    x,y = 0,0
    for c in colors:
        if c:
            x+=1
        else:
            y+=1
    print(x*y - M)
else:
    print((N*(N-1))//2 - M)