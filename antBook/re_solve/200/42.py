import sys
sys.setrecursionlimit(10**9)
N=int(input())
graph=[[] for _ in range(N)]
dp = [[1] * 2 for _ in range(N)]
passed = [False] * N
MOD = 10**9+7
for _ in range(N-1):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
def dfs(x):
    passed[x]=True
    for nx in graph[x]:
        if passed[nx]:continue
        dfs(nx)
        dp[x][0] *= dp[nx][1] + dp[nx][0]
        dp[x][0] %= MOD
        dp[x][1] *= dp[nx][0]
        dp[x][1] %= MOD
dfs(0)
print(sum(dp[0])%MOD)