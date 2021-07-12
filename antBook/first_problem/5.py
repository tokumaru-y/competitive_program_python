V,E,r =list(map(int, input().split()))
graph=[[] for _ in range(V)]
dist=[float("inf")]*V
dist[r]=0
for _ in range(E):
    s,t,x=list(map(int, input().split()))
    graph[s].append([t,x])
is_negative_cycle = False
for cnt in range(V):
    is_update = False
    for v in range(V):
        if dist[v]==float("inf"):continue
        for nv,c in graph[v]:
            if dist[v] + c < dist[nv]:
                dist[nv]=dist[v]+c
                is_update=True
    if not is_update:break
    if cnt==V-1 and is_update:
        is_negative_cycle = True
if is_negative_cycle: 
    print("NEGATIVE CYCLE")
else:
    for v in dist:
        print(v if v != float("inf") else "INF")