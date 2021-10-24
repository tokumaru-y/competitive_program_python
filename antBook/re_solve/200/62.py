N,K=list(map(int, input().split()))
A=[0] + [int(input()) for _ in range(N)]
total_cnt = [0] * (N+1)
for i in range(N):
    total_cnt[i+1]+=total_cnt[i]+A[i+1]
if total_cnt[N] == K:
    print(1)
    exit()
dp = [[float("inf")] * (N+1) for _ in range(N+1)]
dp[0][0]=0
dp[1][0]=0
dp[1][1]=1
for i in range(1,N):
    for j in range(i+1):
        if dp[i][j] != float("inf"):
            needs = (dp[i][j] * A[i+1])//total_cnt[i]
            needs += 1
            if needs+dp[i][j]<= total_cnt[i+1]:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+needs)
        dp[i+1][j]=min(dp[i+1][j], dp[i][j])
for i in reversed(range(N+1)):
    if dp[N][i] <= K:
        print(i)
        exit()