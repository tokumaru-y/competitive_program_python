import heapq
import sys
input = sys.stdin.readline

N,M,X,Y=list(map(int,input().split()))
edges=[[] for _ in range(N)]
for _ in range(M):
    a,b,t,k=list(map(int,input().split()))
    a,b=a-1,b-1
    edges[a].append([b,t,k])
    edges[b].append([a,t,k])

tim=0
q=[[0,X-1]]
heapq.heapify(q)
passed=[False]*N
passed[X-1]=True
times=[float('inf')]*N
# times[X-1]=0
while len(q)>0:
    nowt,n=heapq.heappop(q)
    if times[n]<=nowt:continue
    times[n]=nowt
    passed[n]=True
    for e,t,k in edges[n]:
        if passed[e]:continue
        tt=nowt
        if tt%k!=0:
            tt=tt+(k-(tt%k))
        tt+=t
        # if e==Y-1:
        #     print(tt)
        #     exit()
        # times[e]=tt
        heapq.heappush(q,[tt,e])
print(-1 if times[Y-1] == float('inf') else times[Y-1])