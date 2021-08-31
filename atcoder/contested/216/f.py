MOD = 998244353
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
max_a = max(A)
sort_list = []
for a,b in zip(A,B):
    sort_list.append([a,b])
sort_list.sort()
for i in range(N):
    A[i] = sort_list[i][0]
    B[i] = sort_list[i][1]  
dp = [[0] * (max_a+1) for _ in range(N+1)]
dp[0][0]=1
ans = 0
for i in range(N):
    for j in range(max_a+1):
        dp[i+1][j]=dp[i][j]
        if B[i] <= j:
            dp[i+1][j]+=dp[i][j-B[i]]
            dp[i+1][j]%=MOD
        if j <= A[i] - B[i]:
            ans += dp[i][j]
            ans %= MOD
print(ans)