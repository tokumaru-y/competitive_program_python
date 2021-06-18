N,M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,c])
dist = [float('-inf')] * N
dist[0]=0
is_inf_cycle = False
for count in range(N):
    is_update = False
    for v in range(N):
        if dist[v] == float('-inf'):continue
        for nv, cost in graph[v]:
            if dist[v] + cost > dist[nv]:
                dist[nv] = dist[v] + cost
                is_update = True
    if not is_update:break
    if count == N-1:
        is_inf_cycle = True
        break
if is_inf_cycle:
    print("inf")
else:
    print(dist[N-1])