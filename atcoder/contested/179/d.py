N,K=list(map(int,input().split()))
LR=[list(map(int,input().split())) for _ in range(K)]
MOD=998244353
dp=[0]*(N)
sdp=[0]*(N+1)
dp[0]=1
sdp[1]=1
for i in range(1,N):
    for l,r in LR:
        right = max(0,i-l+1)
        left = max(0,i-r)
        dp[i]+=sdp[right] - sdp[left]
        dp[i]%=MOD
    sdp[i+1]=sdp[i]+dp[i]
print(dp[N-1])