N,K=list(map(int,input().split()))
LR=[list(map(int,input().split())) for _ in range(K)]
dp=[0]*(N+10)
dp[0]=1
for i in range(1,N+1):
    for l,r in LR:
        left=i-l if i-l>0 else 0
        right=i-r if i-r>0 else 0
        dp[i]+=dp[left]
        if left!=right:dp[i]+=dp[right]
print(dp[N])