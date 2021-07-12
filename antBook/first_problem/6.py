N,M=list(map(int, input().split()))
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,-c])
dist=[float("inf")]*N
is_cycle = [False]*N
dist[0]=0
is_inf_cycle = False
for cnt in range(N):
    is_update=False
    for v in range(N):
        if dist[v]==float("inf"):continue
        for nv,cost in graph[v]:
            if dist[nv] > dist[v]+cost:
                dist[nv]=dist[v]+cost
                is_update=True
    if not is_update:break
    if cnt == N-1 and is_update:
        is_inf_cycle=True
for cnt in range(N):
    for v in range(N):
        if dist[v]==float("inf"):continue
        for nv,cost in graph[v]:
            if dist[nv] > dist[v]+cost:
                dist[nv]=dist[v]+cost
                is_cycle[nv]=True
            if is_cycle[v]:
                is_cycle[nv]=True
    if not is_update:break

if is_cycle[N-1]:
    print("inf")
else:
    print(-dist[N-1])