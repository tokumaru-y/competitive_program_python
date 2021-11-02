# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=jp
N,W=list(map(int, input().split()))
dp = [0] * (10**4+1)
VW=[list(map(int, input().split())) for _ in range(N)]
for v,w in VW:
    for _w in range(10**4+1):
        if w+_w <= W:dp[w+_w] = max(dp[w+_w], dp[_w] + v)
print(max(dp))