import heapq
N,M=list(map(int,input().split()))
ABC=[list(map(int,input().split())) for _ in range(N)]
edges=[[float('inf')] * N for _ in range(N)]
ans=[]
for a,b,c in ABC:
    a,b=a-1,b-1
    edges[a][b]=min(edges[a][b],c)
for i in range(N):
    q=[]
    heapq.heapify(q)
    costs=[float('inf')] * N
    heapq.heappush(q,[0,i])
    c = float('inf')
    while len(q) > 0:
        cos,top=heapq.heappop(q)
        if costs[top] < cos:continue
        costs[top]=cos
        if i==0:print(i,cos,top,edges[i])
        for j in range(N):
            tmp = edges[top][j]
            if costs[j] > tmp + cos :
                heapq.heappush(q,[tmp+cos,j])
            if j == i and tmp != float('inf'):
                c=min(c,tmp + cos)
    print(c if c != float('inf') else -1)