V,E,r=list(map(int, input().split()))
graph=[[] for _ in range(V)]
for _ in range(E):
    s,t,w=list(map(int, input().split()))
    graph[s].append([t,w])
ans = [float("inf")]*V
ans[r]=0
for cnt in range(V):
    is_update=False
    for t in range(V):
        if ans[t] == float("inf"):continue
        for nt, nw in graph[t]:
            if ans[nt]<=nw+ans[t]:continue
            is_update=True
            ans[nt]=ans[t]+nw
    if not is_update:break
    if is_update and cnt == V-1:
        print("NEGATIVE CYCLE")
        exit()
for a in ans:
    print(a if a != float("inf") else "INF")
