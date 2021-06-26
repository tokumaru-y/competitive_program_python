H,N=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp=[float("inf")] * (H+1)
dp[0]=0
for h in range(H+1):
    for attack, magic in AB:
        nh = min(H, h+attack)
        dp[nh]=min(dp[nh], dp[h]+magic)
print(dp[H])