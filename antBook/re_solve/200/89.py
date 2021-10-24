N,M,T=list(map(int, input().split()))
A=list(map(int, input().split()))
graph=[[] for _ in range(N)]
back_graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append([b,c])
    back_graph[b].append([a,c])
cost_table = [float("inf")] * N
cost_table[0]=0
back_table = [float("inf")] * N
back_table[0]=0
from heapq import heapify,heappush,heappop
h=[[0,0]]
heapify(h)
while len(h)>0:
    oc,ot=heappop(h)
    for nt,nc in graph[ot]:
        sc=nc+oc
        if cost_table[nt]<=sc:continue
        cost_table[nt]=sc
        heappush(h,[sc,nt])
h=[[0,0]]
heapify(h)
while len(h)>0:
    oc,ot=heappop(h)
    for nt,nc in back_graph[ot]:
        sc=nc+oc
        if back_table[nt]<=sc:continue
        back_table[nt]=sc
        heappush(h,[sc,nt])
ans = 0
for i in range(N):
    if cost_table[i] + back_table[i] > T:continue
    tmp = (T - (cost_table[i] + back_table[i])) * A[i]
    ans=max(ans,tmp)
print(ans)