# https://atcoder.jp/contests/indeednow-qualb/tasks/indeednow_2015_qualc_3
N=int(input())
AB=[list(map(int, input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N)]
for a,b in AB:
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
history = []
passed = [False] * N
from heapq import heapify,heappop,heappush
q = [0]
while len(q)>0:
    v = heappop(q)
    passed[v] = True
    history.append(v+1)
    for nv in graph[v]:
        if passed[nv]:continue
        heappush(q,nv)
print(*history, sep=" ")