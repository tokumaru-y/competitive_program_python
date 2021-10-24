# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=jp
N =int(input())
for _ in range(N):
    S=input()
    T=input()
    ls = len(S)
    lt = len(T)
    dp = [[0] * (lt+1) for _ in range(ls+1)]
    for s in range(ls):
        for t in range(lt):
            if S[s] == T[t]:
                dp[s+1][t+1] = max(dp[s+1][t+1], dp[s][t] + 1)
            else:
                dp[s+1][t+1] = max(dp[s+1][t], dp[s][t+1])
    print(dp[ls][lt])