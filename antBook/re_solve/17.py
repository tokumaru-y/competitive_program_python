N,M=list(map(int, input().split()))
graph = [[float("inf")] * 7 for _ in range(N)]
roads = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    roads[a].append([b,c])
    roads[b].append([a,c])
from heapq import heapify,heappop,heappush
h=[[0,0]]
graph[0][0]=0
heapify(h)
while len(h)>0:
    cost, nx = heappop(h)
    for x, c in roads[nx]:
        next_i = (cost+c)%7
        total_cost = cost+c
        if graph[x][next_i] <= total_cost:continue
        graph[x][next_i] = total_cost
        if x == N-1:
            if (total_cost % 4 ==0 or total_cost % 7 == 0):
                print(total_cost)
                exit()
            else:
                continue
        heappush(h, [total_cost, x])
        