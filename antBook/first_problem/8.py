N,M,R=list(map(int, input().split()))
Rs=list(map(lambda x : int(x)-1, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int ,input().split()))
    a-=1
    b-=1
    graph[a].append([b,c])
    graph[b].append([a,c])
dp = [[float("inf")] * N for _ in range(N)]
for i in range(N):dp[i][i]=0
for i in range(N):
    for x,c in graph[i]:
        dp[i][x] = min(dp[i][x],c)
        dp[x][i] = min(dp[x][i],c)
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
ans = float("inf")
import itertools
for ll in itertools.permutations(Rs):
    tmp = 0
    for i in range(1,R):tmp+=dp[ll[i-1]][ll[i]]
    ans=min(ans,tmp)
print(ans)