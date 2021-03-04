import sys
input = sys.stdin.readline
R,C,K=list(map(int,input().split()))
items = [[0] * C for _ in range(R)]
dp = [[[0,0,0,0] for _ in range(C+1)] for _ in range(R+1)]
for _ in range(K):
    r,c,v=list(map(int,input().split()))
    r,c=r-1,c-1
    items[r][c]+=v
for i in range(1,R+1):
    for j in range(1,C+1):
        for m in range(1,4):
            dp[i][j][0]=max(dp[i-1][j][m],dp[i][j][0])
            dp[i][j][1]=max(dp[i-1][j][m]+items[i-1][j-1], dp[i][j][1])
            dp[i][j][m]=max(dp[i][j-1][m], dp[i][j][m])
            pre = dp[i][j-1][m-1] if m > 0 else 0
            dp[i][j][m]=max(dp[i][j][m], pre+items[i-1][j-1])
print(max(dp[R][C]))