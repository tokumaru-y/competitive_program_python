# https://atcoder.jp/contests/abc153/tasks/abc153_e
H,N=list(map(int,input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp = [float("inf")] * (10**4+1)
dp[H]=0
for a,b in AB:
    for i in reversed(range(10**4+1)):
        life = i - a if i - a > 0 else 0
        if life<=H:dp[life] = min(dp[life], dp[i] + b)
print(dp[0])