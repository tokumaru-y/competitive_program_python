import heapq
import sys
input = sys.stdin.readline
N,M,S,T=list(map(int, input().split()))
S-=1
T-=1
graph = [[]*N for _ in range(N)]
money = [[0]* N for _ in range(N)]
snuuku = [[0] * N for _ in range(N)]
for _ in range(M):
    u,v,a,b = list(map(int, input().split()))
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)
    money[u][v]=a
    money[v][u]=a
    snuuku[u][v]=b
    snuuku[v][u]=b
sum_money = [0]*N
sum_snuuku = [0] * N
h = [[0,S]]
heapq.heapify(h)
passed = [False] * N
passed[S] = True
cnt = 1
while len(h) > 0:
    m,t = heapq.heappop(h)
    for e in graph[t]:
        if passed[e]:continue
        cnt += 1
        passed[e] = True
        cost = m + money[t][e]
        sum_money[e]=cost
        if cnt == N:break
        heapq.heappush(h, [cost, e])

passed=[False]*N
h = [[0,T]]
heapq.heapify(h)
passed[T]=True
cnt = 1
while len(h) > 0:
    s,t = heapq.heappop(h)
    for e in graph[t]:
        if passed[e]:continue
        passed[e]=True
        cost = s + snuuku[t][e]
        sum_snuuku[e]=cost
        cnt +=1
        if cnt == N:break
        heapq.heappush(h, [cost, e])
left = 10**15
min_cost = float('inf')
ans = []
for i in reversed(range(N)):
    min_cost = min(min_cost, sum_money[i]+sum_snuuku[i])
    ans.append(left - min_cost)
ans.reverse()
print(*ans, sep='\n')