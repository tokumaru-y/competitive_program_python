import sys
sys.setrecursionlimit(10**9)
MOD = 998244353
N,M,K=list(map(int, input().split()))
ng_path = [[] for _ in range(N)]
for _ in range(M):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    ng_path[a].append(b)
    ng_path[b].append(a)
dp = [[0] * N for _ in range(K+1)]
dp[0][0]=1
for i in range(K):
    total = sum(dp[i])
    for s in range(N):
        dp[i+1][s] = total - dp[i][s]
        for e in ng_path[s]:
            dp[i+1][s] -= dp[i][e]
        dp[i+1][s]%=MOD
print(dp[K][0]%MOD)