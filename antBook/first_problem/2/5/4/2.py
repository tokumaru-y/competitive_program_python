N,M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,-c])
dist = [float('inf')] * N
dist[0] = 0
for count in range(N):
    is_update = False
    for v in range(N):
        if dist[v] == float('inf'):continue
        for nv, point in graph[v]:
            if dist[nv] > dist[v] + point:
                dist[nv] = dist[v] + point
                is_update = True
    if not is_update:break
negative_flag = [False] * N
for count in range(N):
    for v in range(N):
        if dist[v] == float('inf'):continue
        for nv, point in graph[v]:
            if dist[nv] > dist[v] + point:
                dist[nv] = dist[v] + point
                negative_flag[nv] = True
            if negative_flag[v] == True:
                negative_flag[nv] = True
if negative_flag[N-1]:
    print("inf")
else:
    print(-dist[N-1])