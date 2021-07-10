from heapq import heapify, heappop, heappush
N,K=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(K):
    line=list(map(int, input().split()))
    if line[0]==1:
        pattern, x, y, cost = line
        x-=1
        y-=1
        graph[x].append([y,cost])
        graph[y].append([x,cost])
    else:
        pattern, x, y = line
        x-=1
        y-=1
        h = [[0, x]]
        heapify(h)
        sum_cost = [float('inf')] * N
        sum_cost[x]=0
        while len(h) > 0:
            c, t= heappop(h)
            for nt, nc in graph[t]:
                tmp_cost = c + nc
                if sum_cost[nt] <= tmp_cost: continue
                sum_cost[nt] = tmp_cost
                heappush(h, [tmp_cost, nt])
        ans = sum_cost[y] if sum_cost[y] < float('inf') else -1
        print(ans)
        