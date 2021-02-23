import heapq
H,W=list(map(int,input().split()))
grid=[list(input()) for _ in range(H)]
distances=[[0] * W for _ in range(H)]
MOD=10**9+7
nx=[0,1,1]
ny=[1,1,0]
def bfs(h,w):
    q=[[0,h,w]]
    heapq.heapify(q)
    while len(q) > 0:
        a,b,c=heapq.heappop(q)
        print(a,b)
        for i in range(3):
            nh=a+nx[i]
            nw=b+ny[i]
            if 0<= nh <= H-1 and 0<= nw <= W-1:
                if grid[nh][nw] == "#":continue
                distances[nh][nw]+=c+1
                heapq.heappush(q,[distances[nh][nw],nw,nw])
    print(distances[H-1][W-1])
bfs(0,0)
print(distances[H-1][W-1])