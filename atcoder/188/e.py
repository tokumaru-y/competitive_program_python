from collections import deque
n,m=list(map(int,input().split()))
costs=list(map(int,input().split()))
edges=[deque() for _ in range(n)]
for _ in range(m):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    edges[a].append(b)
dp=[float('inf') for _ in range(n)]

for i in range(n):
    nodes=edges[i]
    while len(nodes) > 0:
        next_node=nodes.pop()
        dp[next_node]=min(dp[i],dp[next_node],costs[i])
ans=float('-inf')
for i in range(n):
    ans=max(ans,costs[i]-dp[i])
print(ans)