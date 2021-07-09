N,M,T=list(map(int, input().split()))
A=list(map(int, input().split()))
go_graph=[[] for _ in range(N)]
back_graph=[[] for _ in range(N)]
go=[float("inf")] * N
back=[float("inf")] * N
go[0]=0
back[0]=0
for _ in range(M):
    a,b,c=list(map(int, input().split()))
    a-=1
    b-=1
    go_graph[a].append([b,c])
    back_graph[b].append([a,c])
from heapq import heapify,heappush,heappop
h=[[0,0]]
heapify(h)
while len(h)>0:
    tmp_cost, top = heappop(h)
    for nx, c in go_graph[top]:
        total = tmp_cost+c
        if go[nx] <= total:continue
        go[nx] = total
        heappush(h, [total, nx])
h=[[0,0]]
heapify(h)
while len(h)>0:
    tmp_cost, top = heappop(h)
    for nx, c in back_graph[top]:
        total = tmp_cost+c
        if back[nx] <= total:continue
        back[nx] = total
        heappush(h, [total, nx])
ans = float("-inf")
for i in range(N):
    left_time = T - (go[i]+back[i])
    ans = max(ans, A[i]*left_time)
print(ans)