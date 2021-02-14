N=int(input())
dp=[0]*(N+1)
dp[0]=1
total_cnt = 2
for i in range(1,N+1):
    s=input().rstrip()
    if s=="AND":
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + total_cnt
    total_cnt += 2**(i)
print(dp[-1])