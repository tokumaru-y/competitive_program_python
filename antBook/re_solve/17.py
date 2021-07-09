N,M=list(map(int, input().split()))
fgraph = [[float("inf")] * 4 for _ in range(N)]
sgraph = [[float("inf")] * 7 for _ in range(N)]
roads = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    roads[a].append([b,c])
    roads[b].append([a,c])
from heapq import heapify,heappop,heappush
h=[[0,0]]
heapify(h)
ans = [float("inf"), float("inf")]
while len(h) > 0:
    cost, nx = heappop(h)
    for x,c in roads[nx]:
        total_cost = cost+c
        ni = total_cost%4
        if fgraph[x][ni] <= total_cost:continue
        fgraph[x][ni]=total_cost
        if x == N-1:
            if ni == 0:
                ans[0]=total_cost
                h=[]
                break
            else:continue
        heappush(h, [total_cost, x])
h=[[0,0]]
while len(h) > 0:
    cost, nx = heappop(h)
    for x,c in roads[nx]:
        total_cost = cost+c
        ni = total_cost%7
        if sgraph[x][ni] <= total_cost:continue
        sgraph[x][ni]=total_cost
        if x == N-1:
            if ni == 0:
                ans[1]=total_cost
                h=[]
                break
            else:continue
        heappush(h, [total_cost, x])

print(min(ans))