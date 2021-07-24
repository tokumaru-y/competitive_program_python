N,D=list(map(int, input().split()))
# 2は60,3は40,5は30
dp = [[[[0] * 31 for _ in range(41)] for _ in range(61)] for _ in range(N+1)]
target = [0,0,0]
div = [2,3,5]
for ind in range(3):
    d = div[ind]
    while D%d==0:
        target[ind]+=1
        D//=d
if D!=1:
    print(0)
    exit()
dp[0][0][0][0]=1
for n in range(N):
    for i in range(61):
        for j in range(41):
            for k in range(31):
                ni = min(i,target[0])
                nj = min(j,target[1])
                nk = min(k,target[2])
                dp[n+1][ni][nj][nk] += dp[n][i][j][k] / 6
                if 0<=i-1:dp[n+1][ni][nj][nk] += dp[n][i-1][j][k] / 6
                if 0<=i-2:dp[n+1][ni][nj][nk] += dp[n][i-2][j][k] / 6
                if 0<=j-1:dp[n+1][ni][nj][nk] += dp[n][i][j-1][k] / 6
                if 0<=i-1 and 0<=j-1:dp[n+1][ni][nj][nk] += dp[n][i-1][j-1][k] / 6
                if 0<=k-1:dp[n+1][ni][nj][nk] += dp[n][i][j][k-1] /6
print(dp[N][target[0]][target[1]][target[2]])