# https://atcoder.jp/contests/abc015/tasks/abc015_4
W=int(input())
N,K=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp = [[float("-inf")] * (W+1) for _ in range(K+1)]
dp[0][0]=0
for i in range(N):
    width, value = AB[i]
    for j in reversed(range(K)):
        for w in reversed(range(W+1)):
            if w + width <= W and dp[j][w] > float("-inf"):
                dp[j+1][w+width] = max(dp[j+1][w+width], dp[j][w] + value)
ans = 0
for j in range(K+1):
    for w in range(W+1):
        ans = max(ans, dp[j][w])
print(ans)