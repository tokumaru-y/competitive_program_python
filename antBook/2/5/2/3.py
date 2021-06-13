from heapq import heapify, heappush, heappop
N,M,T=list(map(int, input().split()))
money = list(map(int, input().split()))
graph = [[] for _ in range(N)]
reverse_graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,c])
    reverse_graph[b].append([a,c])
sum_cost = [float('inf')] * N
reverse_cost = [float('inf')] * N
def dijkstra(h, graph, cost_list):
    heapify(h)
    while len(h) > 0:
        c,t = heappop(h)
        for e,cost in graph[t]:
            tmp_cost=c+cost
            if cost_list[e] <= tmp_cost:continue
            cost_list[e] = tmp_cost
            heappush(h, [tmp_cost, e])
sum_cost[0] = 0
reverse_cost[0] = 0
dijkstra([[0,0]], graph, sum_cost)
dijkstra([[0,0]], reverse_graph, reverse_cost)
ans = 0
for i in range(N):
    max_count = max(money[0], money[i])
    passed_time = sum_cost[i] + reverse_cost[i]
    tmp_ans = T - passed_time if T - passed_time >= 0 else float('-inf')
    ans = max(ans, max_count * tmp_ans)
print(ans)