# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_E&lang=jp
S=input()
T=input()
len_s = len(S)
len_t = len(T)
dp = [[float("inf")] * (len_t+1) for _ in range(len_s+1)]
for i in range(len_s+1):dp[i][0] = i
for i in range(len_t+1):dp[0][i] = i
for i in range(len_s):
    for j in range(len_t):
        if S[i] == T[j]:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
        else:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j]+1)
print(dp[len_s][len_t])