import heapq
import sys
input = sys.stdin.readline
N,M,S,T=list(map(int, input().split()))
S-=1
T-=1
graph_money = [[]*N for _ in range(N)]
graph_snuuke = [[] * N for _ in range(N)]
for _ in range(M):
    u,v,a,b = list(map(int, input().split()))
    u-=1
    v-=1
    graph_money[u].append([a,v])
    graph_money[v].append([a,u])
    graph_snuuke[u].append([b, v])
    graph_snuuke[v].append([b, u])
sum_money = [float('inf')]*N
sum_snuuku = [float('inf')] * N
h = [[0,S]]
sum_money[S]=0
sum_snuuku[T]=0
heapq.heapify(h)
cnt = 0
while len(h) > 0:
    cnt += 1
    if cnt == N:break
    m,t = heapq.heappop(h)
    for money,e in graph_money[t]:
        cost = m + money
        if sum_money[e] <= cost:continue
        sum_money[e]=cost
        heapq.heappush(h, [cost, e])

h = [[0,T]]
heapq.heapify(h)
cnt = 0
while len(h) > 0:
    cnt += 1
    if cnt == N:break
    s,t = heapq.heappop(h)
    for snuuku,e in graph_snuuke[t]:
        cost = s + snuuku
        if sum_snuuku[e] <= cost:continue
        sum_snuuku[e]=cost
        heapq.heappush(h, [cost, e])
left = 10**15
min_cost = float('inf')
ans = []
for i in reversed(range(N)):
    min_cost = min(min_cost, sum_money[i]+sum_snuuku[i])
    ans.append(left - min_cost)
ans.reverse()
print(*ans, sep='\n')