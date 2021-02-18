import sys
input = sys.stdin.readline
from collections import deque


N,M=list(map(int,input().split()))
A=list(map(int,input().split()))
XY=[list(map(lambda x : int(x)-1, input().split())) for _ in range(M)]
# 買った最小金額
dp=[float('inf')] * N
edges=[[] for _ in range(N)]
for x,y in XY:
    edges[x].append(y)
ans=float('-inf')
for i in range(N):
    if dp[i]!=float('inf'):continue
    # dp[i]=A[i]
    q=deque([i])
    while len(q) > 0:
        n = q.popleft()
        if edges[n]:
            for e in edges[n]:
                if dp[e] <= min(dp[n],A[n]):continue
                dp[e]=min(dp[n],A[n])
                q.append(e)
for i in range(N):
    ans=max(ans,A[i]-dp[i])
print(ans)