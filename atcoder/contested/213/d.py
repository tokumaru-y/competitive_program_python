import sys
sys.setrecursionlimit(10**9)
from heapq import heapify,heappop,heappush
N=int(input())
passed=[False]*N
graph =[[] for _ in range(N)]
for _ in range(N-1):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
for i in range(N):
    graph[i]=sorted(graph[i])
ans=[]
def dfs(v,parent):
    ans.append(v+1)
    passed[v] = True
    for next_v in graph[v]:
        if passed[next_v]:continue
        dfs(next_v,v) 
    if v > 0:ans.append(parent+1)

passed[0]=True
dfs(0,0)
print(*ans)