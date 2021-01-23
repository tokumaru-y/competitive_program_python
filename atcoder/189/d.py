n=int(input())
ll=[input() for _ in range(n)]
dp=[0]*(n+1)
dp[0]=1
cnt=2
for ind,l in enumerate(ll):
    if l=="AND":
        dp[ind+1]=dp[ind]
    else:
        dp[ind+1]=dp[ind] + cnt
    cnt*=2
print(dp[n])