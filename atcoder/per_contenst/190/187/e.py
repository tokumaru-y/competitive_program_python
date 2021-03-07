import collections
from typing import Deque


N=int(input())
edges=[[] for _ in range(N)]
AB=[]
costs=[0]*N
deepth=[float('inf')]*N
for _ in range(N-1):
    a,b=list(map(int,input().split()))
    a,b=a-1,b-1
    edges[a].append(b)
    edges[b].append(a)
    AB.append([a,b])
def dfs(t,value):
    q=collections.deque([t])
    passed=[False]*N
    passed[0]=True
    while len(q) > 0:
        n = q.popleft()
        for e in edges[n]:
            if passed[e]:continue
            passed[e]=True
            deepth[e]=deepth[n]+1
            q.append(e)
deepth[0]=1
dfs(0,1)
Q=int(input())
all_num=0
for _ in range(Q):
    t,e,x=list(map(int,input().split()))
    e-=1
    a,b=AB[e]
    if t==2:a,b=b,a
    if deepth[a] < deepth[b]:
        all_num+=x
        costs[b]-=x
    else:
        costs[a]+=x
passed=[False]*N
passed[0]=True
costs[0]+=all_num
q=collections.deque([0])
while len(q) > 0:
    n = q.popleft()
    if len(edges[n]) <= 0:continue
    for e in edges[n]:
        if passed[e]:continue
        passed[e]=True
        q.append(e)
        costs[e]+=costs[n]
print(*costs,sep='\n')