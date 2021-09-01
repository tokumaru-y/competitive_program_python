MOD=998244353
N=int(input())
S=input().rstrip()
dp = [[[0] * 11 for _ in range(1<<10)] for _ in range(N+1)]
num_list = {}
for i in range(65, 75):
    num_list[chr(i)] = i-65
dp[0][0][0]=1
for i in range(N):
    for j in range(1<<10):
        for k in range(11):
            if dp[i][j][k] == 0:continue
            dp[i+1][j][k]+=dp[i][j][k]
            target = S[i]
            target_num = num_list[target]
            if ((j & 1<<target_num) and k!=target_num):continue
            dp[i+1][j | (1<<target_num)][target_num] += dp[i][j][k]
            dp[i+1][j | (1<<target_num)][target_num] %=MOD
ans = 0
for i in range(1, 1<<10):
    for j in range(11):
        ans+=dp[N][i][j]
        ans%=MOD
print(ans)