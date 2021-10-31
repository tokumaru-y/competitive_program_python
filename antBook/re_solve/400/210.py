# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
N=int(input())
P=list(map(int, input().split()))
dp = [float("inf")] * (100*100 + 1)
dp[0] = 0
for p in P:
    for i in reversed(range(100*100+1)):
        if dp[i] < float("inf"):dp[i+p] = dp[i] + 1
ans = 0
for i in range(100*100 + 1):
    if dp[i] < float("inf"):ans+=1
print(ans)