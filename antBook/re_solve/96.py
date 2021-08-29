# まず、入力されたものをマイナスに変換。そのあと、一度ベルマンフォードで検出。その際、サイクルを検出し、もう一度回す。すると、Nでその負のサイクルが検出されたらinfとする。
N,M=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,-c])
dist=[float("inf")] * N
is_negative_cycle = False
is_cycle = [False] * N
dist[0]=0
for i in range(N):
    is_update = False
    for v in range(N):
        if dist[v] == float("inf"):continue
        for nv,nw in graph[v]:
            if dist[v] + nw < dist[nv]:
                dist[nv]=dist[v]+nw
                is_update = True
    if not is_update:continue
for i in range(N):
    for v in range(N):
        if dist[v] == float("inf"):continue
        for nv, nw in graph[v]:
            if dist[v] + nw < dist[nv]:
                dist[nv] = dist[v] + nw
                is_cycle[nv] = True
            if is_cycle[v]:
                is_cycle[nv]=True
if is_cycle[N-1]:
    print("inf")
else:
    print(-1*dist[N-1])