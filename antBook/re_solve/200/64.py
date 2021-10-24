N,M,X=list(map(int, input().split()))
trees = [int(input()) for _ in range(N)]
graph = [[] * N for _ in range(N)]
for _ in range(M):
    a,b,t=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,t])
    graph[b].append([a,t])
from heapq import heapify, heappop, heappush
h = [[0,0,X]]
heapify(h)
costs = [float("inf")] * N
costs[0] = 0
last_height = 0
while len(h)>0:
    cst, top, heigh = heappop(h)
    for nt,dist in graph[top]:
        if costs[nt] <= cst:continue
        if trees[top] - dist < 0:continue
        next_height = heigh
        next_cost = cst + dist
        if next_height - dist < 0:
            next_cost += dist - next_height
            next_height = 0
        elif next_height - dist > trees[nt]:
            next_cost += (next_height - dist) - trees[nt]
            next_height = trees[nt]
        else:
            next_height -= dist
        if costs[nt] > next_cost:
            if nt == N-1:
                last_height = max(last_height, next_height)
            costs[nt] = next_cost
            heappush(h, [next_cost, nt, next_height])
print(costs[N-1]+abs(trees[N-1] - last_height) if costs[N-1] != float("inf") else -1)