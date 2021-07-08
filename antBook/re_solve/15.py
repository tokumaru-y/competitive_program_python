from heapq import heapify,heappop,heappush
N,K=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(K):
    inp = list(map(int, input().split()))
    if inp[0] == 0:
        cost = [float("inf")] * N
        h = [[0,inp[1]-1]]
        heapify(h)
        while len(h)>0:
            m,nx = heappop(h)
            for x, c in graph[nx]:
                total = m+c
                if cost[x] <= total:continue
                cost[x]=total
                heappush(h, [total, x])
        ans = cost[inp[2]-1]
        print(ans if ans != float("inf") else -1)
    else:
        _, c,d,e = inp
        c-=1
        d-=1
        graph[c].append([d,e])
        graph[d].append([c,e])