from heapq import heapify,heappop,heappush
N=int(input())
graph = [[] for _ in range(N)]
for i in range(N-1):
    a,b,c=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,c])
    graph[b].append([a,c])
dp=[float("inf")]*N
Q,K=list(map(int, input().split()))
K-=1
dp[K]=0
h = [[0,K]]
heapify(h)
while len(h) >0:
    cost, x = heappop(h)
    for nx,tmp_cost in graph[x]:
        total_cost = cost + tmp_cost
        if dp[nx] <= total_cost:continue
        dp[nx]=total_cost
        heappush(h, [total_cost, nx])

for _ in range(Q):
    x,y=list(map(int, input().split()))
    x-=1
    y-=1
    print(dp[x]+dp[y])