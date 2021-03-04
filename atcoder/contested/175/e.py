R,C,K=list(map(int,input().split()))
items = [[0] * C for _ in range(R)]
dp = [[0] * (C+1) for _ in range(R+1)]
for _ in range(K):
    r,c,v=list(map(int,input().split()))
    r,c=r-1,c-1
    items[r][c]+=v
for i in range(1,R+1):
    for j in range(1,C+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        dp[i][j]+=items[i-1][j-1]
print(dp[R][C])