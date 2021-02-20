import collections
from typing import Deque


N=int(input())
edges=[[] for _ in range(N)]
costs=[0]*N
deepth=[float('inf')]*N
for _ in range(N-1):
    a,b=list(map(int,input().split()))
    a,b=a-1,b-1
    edges[a].append(b)
    edges[b].append(a)
def dfs(t,value,array):
    if len(edges[t]) > 0:
        for e in edges[t]:
            if array[e]!=float('inf'):continue
            array[e]=value+1
            dfs(e,value+1,array)
deepth[0]=1
dfs(0,1,deepth)
Q=int(input())
all_num=0
for _ in range(Q):
    t,e,x=list(map(int,input().split()))
    e-=1
    if t==2:a,b=b,a
    if deepth[a] > deepth[b]:
        all_num+=x
        costs[b]-=x
    else:
        costs[a]+=x
passed=[False]*N
passed[0]=True
q=collections.deque([[0,0]])
while len(q) > 0:
    n,c = q.popleft()
    if passed[n] or len(edges[n]) <= 0:continue
    for e in edges[n]:
        if passed[e]:continue
        passed[e]=True
        q.append([e,c+costs[e]])
        costs[e]+=all_num+c
print(*costs,sep='\n')