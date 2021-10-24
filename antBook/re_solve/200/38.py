A,B=list(map(int, input().split()))
As=list(map(int, input().split()))
Bs=list(map(int, input().split()))
dp = [[0] * (B+1) for _ in range(A+1)]
# 左にA、右にB残っているときの値
dp[A][B]=0
for i in reversed(range(A+1)):
    for j in reversed(range(B+1)):
        if i == A and j == B:continue
        if (i+j)%2==0:
            if i == A:
                dp[i][j] = Bs[j] + dp[i][j+1]
            elif j == B:
                dp[i][j] = As[i] + dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j] + As[i], dp[i][j+1] + Bs[j])
        else:
            if i == A:
                dp[i][j] = dp[i][j+1]
            elif j == B:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])
print(dp[0][0])