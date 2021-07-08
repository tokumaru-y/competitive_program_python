from heapq import heapify, heappop, heappush
N,M,S,T=list(map(int, input().split()))
yen = [float("inf")] * N
snuuke = [float("inf")] * N
graph_yen = [[] for _ in range(N)]
graph_snuuke = [[] for _ in range(N)]
for _ in range(M):
    u,v,a,b = list(map(int, input().split()))
    u-=1
    v-=1
    graph_yen[u].append([v,a])
    graph_yen[v].append([u,a])
    graph_snuuke[u].append([v,b])
    graph_snuuke[v].append([u,b])
S-=1
T-=1
yen[S] = 0
snuuke[T] = 0

h = [[0,S]]
passed = [False] * N
passed[S] = True
heapify(h)
while len(h) > 0:
    cost, nx = heappop(h)
    for v, c in graph_yen[nx]:
        if passed[v]:continue
        passed[v] = True
        yen[v]=min(yen[v], cost+c)
        heappush(h, [cost+c, v])
h = [[0, T]]
passed = [False] * N
passed[T]=True
heapify(h)
while len(h) > 0:
    cost, nx = heappop(h)
    for v, c in graph_snuuke[nx]:
        if passed[v]:continue
        passed[v] = True
        snuuke[v]=min(snuuke[v], cost+c)
        heappush(h, [cost+c, v])

ans = float("inf")
ll = []
for i in reversed(range(N)):
    ans = min(ans, yen[i] + snuuke[i])
    ll.append(10**15 - ans)
print(*list(reversed(ll)), sep="\n")