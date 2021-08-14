import sys

sys.setrecursionlimit(10**9)
N=int(input())
UVW=[list(map(int, input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N)]
for u,v,w in UVW:
    graph[u-1].append([v-1,w])
    graph[v-1].append([u-1,w])
#dp[i]:=i二いくまでの最大値
dp = [0] * N
passed = [False] * N
par = [0] * N
def dfs(t, v):
    next = graph[t]
    for top, w in next:
        if passed[top]:continue
        par[top] = t
        dp[top] = max(v, w)
        passed[top]=True
        dfs(top, dp[top])
passed[0]=True
dfs(0,0)
ans = 0
for i in range(1,N):
    if par[i] != i-1:
        ans += dp[par[i]] * i
    else:
        ans += dp[i] * i
print(ans)