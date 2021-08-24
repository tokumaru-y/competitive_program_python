N,M=list(map(int, input().split()))
four_graph = [[float("inf")] * 4 for _ in range(N)]
seven_graph = [[float("inf")] * 7 for _ in range(N)]
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    graph[a].append([b,c])
    graph[b].append([a,c])
ans = float("inf")
from heapq import heappush,heapify,heappop
def set_graph(target):
    if target == 4:
        target_graph = four_graph
    else:
        target_graph = seven_graph
    h = [[0,0]]
    heapify(h)
    target_graph[0][0]=0
    while len(h) > 0:
        oc,ot = heappop(h)
        for nt,nc in graph[ot]:
            sc = oc+nc
            next_num = sc % target
            if target_graph[nt][next_num] <= sc:continue
            target_graph[nt][next_num] = sc
            if nt == N-1:
                if next_num == 0:
                    return sc
                else:
                    continue
            heappush(h,[sc,nt])
    return float("inf")
ans = set_graph(4)
ans = min(ans, set_graph(7))
print(ans)