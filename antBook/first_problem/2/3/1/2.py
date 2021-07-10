N=int(input())
LEN = 100**2 + 1
dp=[[0] * LEN for _ in range(N+1)]
dp[0][0]=1
p_list=list(map(int, input().split()))
for i in range(N):
    for j in range(LEN):
        sum_p=p_list[i]+j
        if dp[i][j]>0 and sum_p <= (LEN-1):
            dp[i+1][sum_p] = dp[i][j]
        dp[i+1][j]=max(dp[i+1][j], dp[i][j])
print(dp[N].count(1))