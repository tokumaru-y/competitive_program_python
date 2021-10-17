from collections import deque
from heapq import heapify, heappop, heappush
N,M=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]
in_cnt = [0] * N
order = []
for a, b in AB:
    a -= 1
    b -= 1
    in_cnt[b]+=1
    graph[a].append(b)
que = [i for i in range(N) if in_cnt[i] == 0]
heapify(que)
seen = [False] * N
while len(que) > 0:
    v = heappop(que)
    order.append(v+1)
    seen[v] = True
    for v2 in graph[v]:
        in_cnt[v2] -= 1
        if in_cnt[v2] == 0:
            heappush(que, v2)
if sum(in_cnt) > 0:
    print(-1)
else:
	print(*order, sep=" ")