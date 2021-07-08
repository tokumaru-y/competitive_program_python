N,M,T=list(map(int, input().split()))
A=list(map(int, input().split()))
graph=[[] for _ in range(N)]
cost=[[float("inf")] * N for _ in range(N)]
cost[0][0]=0
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,c])
    graph[b].append([a,c])
h=[[0,0]]
from heapq import heapify,heappush,heappop
heapify(h)
while len(h)>0:
    tmp_cost, top = heappop(h)
    for nx, c in graph[top]:
        total = tmp_cost+c
        if cost[0][nx] <= total:continue
        cost[0][nx] = total
        heappush(h, [total, nx])
for i in range(1,N):
    h=[[0,i]]
    heapify(h)
    tmp_list = [float("inf")] * N
    tmp_list[i]=0
    while len(h)>0:
        tmp_cost, top = heappop(h)
        for nx, c in graph[top]:
            total = tmp_cost+c
            if tmp_list[nx] <= total:continue
            tmp_list[nx] = total
            heappush(h, [total, nx])
    cost[i][0]=tmp_list[0]
ans = float("-inf")
for i in range(N):
    left_time = T - (cost[0][i]+cost[i][0])
    ans = max(ans, A[i]*left_time)
print(ans)