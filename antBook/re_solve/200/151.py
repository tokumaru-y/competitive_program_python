# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_E&lang=jp
S=input()
T=input()
ls=len(S)
lt=len(T)
dp = [[float("inf")] * (lt+1) for _ in range(ls+1)]
for i in range(ls):
    dp[i+1][0]=i+1
for i in range(lt):
    dp[0][i+1]=i+1
dp[0][0]=0
for s in range(ls):
    for t in range(lt):
        if S[s] == T[t]:
            dp[s+1][t+1] = min([dp[s+1][t+1], dp[s][t]])
        else:
            dp[s+1][t+1] = min(dp[s+1][t+1], dp[s][t]+1,  dp[s+1][t]+1, dp[s][t+1]+1)
print(dp[ls][lt]) 