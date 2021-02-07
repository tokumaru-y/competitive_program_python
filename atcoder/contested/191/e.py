import heapq
N,M=list(map(int,input().split()))
ABC=[list(map(int,input().split())) for _ in range(M)]
edges={}
ans=[]
for a,b,c in ABC:
    a,b=a-1,b-1
    if a in edges:
        if b in edges[a]:
            edges[a][b]=min(edges[a][b],c)
        else:
            edges[a][b]=c
    else:
        edges[a]={b:c}
for i in range(N):
    q=[]
    heapq.heapify(q)
    costs=[float('inf')] * N
    heapq.heappush(q,[0,i])
    c = float('inf')
    while len(q) > 0:
        cos,top=heapq.heappop(q)
        if top not in edges:continue
        for k,v in edges[top].items():
            tmp_cnt=v + cos
            if costs[k] > tmp_cnt:
                costs[k]=tmp_cnt
                heapq.heappush(q,[tmp_cnt,k])
            if i == k and not top == k and tmp_cnt != float('inf'):
                c = min(c,tmp_cnt)
                q=[]
                break
    if i in edges[i]:c = min(c,edges[i][i])
    print(c if c != float('inf') else -1)