import sys
input = sys.stdin.readline
R,C,K=list(map(int,input().split()))
items = [[0] * C for _ in range(R)]
dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]
for _ in range(K):
    r,c,v=list(map(int,input().split()))
    r,c=r-1,c-1
    items[r][c]+=v
for i in range(1,R+1):
    for j in range(1,C+1):
        for m in range(1,4):
            dp[0][i][j]=max(dp[m][i-1][j],dp[0][i][j])
            dp[1][i][j]=max(dp[m][i-1][j]+items[i-1][j-1], dp[1][i][j])
            dp[m][i][j]=max(dp[m][i][j-1], dp[m][i][j])
            dp[m][i][j]=max(dp[m][i][j], dp[m-1][i][j-1]+items[i-1][j-1])
print(max(dp[0][R][C],dp[1][R][C],dp[2][R][C],dp[3][R][C]))
