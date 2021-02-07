import heapq
N,M=list(map(int,input().split()))
ABC=[list(map(int,input().split())) for _ in range(M)]
link=[[] for _ in range(N)]
for a,b,c in ABC:
    a,b=a-1,b-1
    link[a].append([b,c])

for i in range(N):
    dist=[float('inf')] * N
    s = i 
    dist[s]=0
    ans=float('inf')
    h=[]
    heapq.heappush(h,[dist[s],s])
    while len(h) > 0:
        d,v=heapq.heappop(h)
        if d > dist[v]: continue
        for top,cost in link[v]:
            if top == i:
                ans=min(ans,dist[v]+cost)
            else:
                if dist[top] > dist[v]+cost:
                    dist[top] = dist[v] + cost
                    heapq.heappush(h, [dist[top],top])
    print(-1 if ans==float('inf') else ans)