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
heapify(h)
while len(h) > 0:
    cost, nx = heappop(h)
    for v, c in graph_yen[nx]:
        total_cost = cost+c
        if yen[v] <= total_cost:continue
        yen[v]=total_cost
        heappush(h, [cost+c, v])
h = [[0, T]]
heapify(h)
while len(h) > 0:
    cost, nx = heappop(h)
    for v, c in graph_snuuke[nx]:
        total_cost=cost+c
        if snuuke[v] <= total_cost:continue
        snuuke[v]=cost+c
        heappush(h, [cost+c, v])

ans = float("inf")
ll = []
for i in reversed(range(N)):
    ans = min(ans, yen[i] + snuuke[i])
    ll.append(10**15 - ans)
print(*list(reversed(ll)), sep="\n")