# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=jp
N,W=list(map(int, input().split()))
VW=[list(map(int, input().split())) for _ in range(N)]
dp = [0] * (W+1)
for i in range(N):
    v,w = VW[i]
    for j in range(W+1):
        nw = w+j
        if nw<=W:
            dp[nw]=max(dp[nw], dp[j]+v)
print(max(dp))