# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp
N,M=list(map(int, input().split()))
C=list(map(int, input().split()))
dp = [float("inf")] * (N+1)
dp[0]=0
for i in range(N+1):
    for c in C:
        if i+c<=N:
            dp[i+c] = min(dp[i+c],dp[i] + 1)
print(dp[N])
