n,m=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp = [[float('inf')] * (m+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n+1):
    for j in range(m+1):
        if i>0:
            dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
        if j>0:
            dp[i][j] = min(dp[i][j],dp[i][j-1]+1)
        if i > 0 and j > 0:
            if A[i-1] == B[j-1]:
                dp[i][j]=min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j]=min(dp[i][j],dp[i-1][j-1]+1)
print(dp[n][m])