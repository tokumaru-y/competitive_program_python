H,N=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp=[float("inf")] * (H+1)
dp[0]=0
for a,b in AB:
    for i in range(H+1):
        next = i+a if i+a<=H else H
        dp[next]=min(dp[next], dp[i]+b)
print(dp[H])