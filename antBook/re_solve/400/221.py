# https://atcoder.jp/contests/maximum-cup-2018/tasks/maximum_cup_2018_d
N,M,L,X=list(map(int, input().split()))
A=list(map(int, input().split()))
dp = [[float("inf")] * (M) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    gas = A[i]
    for j in range(M):
        if dp[i][j] == float("inf"):continue
        dp[i+1][(j+gas)%M] = min(dp[i+1][(j+gas)%M], dp[i][j] + (j+gas)//M)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
ans = "Yes" if dp[N][L] < X else "No"
print(ans)
