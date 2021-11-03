# https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho4
from heapq import heapify, heappop,heappush
N,M,X=list(map(int, input().split()))
T=[int(input()) for _ in range(N)]
graph = [[] for _ in range(N)]
for _ in range(M):
    x,y,t = list(map(int, input().split()))
    x-=1
    y-=1
    graph[x].append([y,t])
    graph[y].append([x,t])
hq=[[0,X,0]]
heapify(hq)
passed = [False] * N
while len(hq) > 0:
    time, height, node = heappop(hq)
    if passed[node]:continue
    passed[node] = True
    if node == N-1:
        print(time + T[node] - height)
        exit()
    for nv,need_time in graph[node]:
        if passed[nv]:continue
        # 物理的に到達不可能
        if T[node] - need_time < 0:continue
        # 高さ調整
        next_hight,total_time = height - need_time, time + need_time
        if height - need_time > T[nv]:
            total_time += height - need_time - T[nv]
            next_hight = T[nv]
        elif height - need_time < 0:
            total_time += abs(height - need_time)
            next_hight = 0
        heappush(hq, [total_time, next_hight,nv])
print(-1)