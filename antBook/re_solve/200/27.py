H,N=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp = [float("inf")] * (10**4+1)
dp[H] = 0
for a,b in AB:
    for h in reversed(range(10**4+1)):
        nex_h = max(0, h-a)
        dp[nex_h] = min(dp[nex_h], dp[h]+b)
print(dp[0])