N,M=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = list(map(lambda x :int(x)-1, input().split()))
    graph[a].append(b)
    graph[b].append(a)
passed = [False] * N
passed[0]=True
ans = 0
def dfs(v, cnt):
    if cnt == N:
        global ans
        ans += 1
        return
    if len(graph[v]) != 0:
        for nv in graph[v]:
            if passed[nv]:continue
            passed[nv] = True
            dfs(nv, cnt+1)
            passed[nv] = False
dfs(0,1)
print(ans)