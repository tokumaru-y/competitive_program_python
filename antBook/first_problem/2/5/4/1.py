V,E,r = list(map(int, input().split()))
graph = [[] for _ in range(V)]
for _ in range(E):
    s,t,d = list(map(int, input().split()))
    graph[s].append([t,d])
dist = [float('inf')] * V
dist[r] = 0
is_negative_cicle = False
for count in range(V):
    is_update = False
    for v in range(V):
        if dist[v] == float('inf'):continue
        for nv, cost in graph[v]:
            if dist[v] + cost < dist[nv]:
                is_update = True
                dist[nv]=dist[v]+cost
    if not is_update:break
    if count == V-1:
        is_negative_cicle = True
        break
if is_negative_cicle:
    print("NEGATIVE CYCLE")
else:
    for d in dist:
        if d == float('inf'):
            print("INF")
        else:
            print(d)