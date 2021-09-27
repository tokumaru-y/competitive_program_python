# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
N=int(input())
P=list(map(int, input().split()))
dp = [[0] * (10**4+1) for _ in range(N+1)]
dp[0][0]=1
for i in range(N):
    for j in range(10**4+1):
        t=P[i]+j
        if t<=10**4:
            dp[i+1][t]=max(dp[i+1][t], dp[i][j])
        dp[i+1][j]=max(dp[i+1][j], dp[i][j])
print(sum(dp[N]))