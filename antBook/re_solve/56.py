D=int(input())
N=list(input().rstrip())
MOD = 10**9+7
#dp[i][j][k]:=jが1のときは以下のもののみ
dp = [[[0] * D for _ in range(2)] for _ in range(len(N)+1)]
dp[0][0][0]=1
for i in range(len(N)):
    for j in range(D):
        limit = int(N[i])
        for d in range(10):
            dp[i+1][1][(j+d)%D]+=dp[i][1][j]
            dp[i+1][1][(j+d)%D]%=MOD
        for d in range(limit):
            dp[i+1][1][(j+d)%D]+=dp[i][0][j]
            dp[i+1][1][(j+d)%D]%=MOD
        dp[i+1][0][(j+limit)%D]+=dp[i][0][j]
print((dp[len(N)][1][0] + dp[len(N)][0][0] - 1)%MOD)