N=int(input())
A,B=list(map(int, input().split()))
C=int(input())
costs=[int(input()) for _ in range(N)]
dp = [float("inf")] * (N+1)
dp[0] = 0
costs.sort(reverse=True)
ans = float("-inf")
for i in range(N):
    dp[i+1] = dp[i] + costs[i]
    ans = max(ans, (dp[i+1]+C)//(A+(i+1)*B))
print(ans)