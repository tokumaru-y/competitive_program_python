N,Z,W=list(map(int, input().split()))
A=list(map(int, input().split()))
dp = [[0] * 2 for _ in range(N)]
for i in reversed(range(N)):
    dp[i][0]=float("-inf")
    X = A[i-1] if i >0 else W
    dp[i][0]=max(dp[i][0], abs(X-A[N-1]))
    for k in range(i+1,N):
        dp[i][0]=max(dp[i][0], dp[k][1])
    dp[i][1]=float('inf')
    Y = A[i-1] if i >0 else Z
    dp[i][1]=min(dp[i][1], abs(Y-A[N-1]))
    for k in range(i+1,N):
        dp[i][1]=min(dp[i][1], dp[k][0])
print(dp[0][0])