# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=jp
# TLE
# N=int(input())
# for _ in range(N):
#     S=input()
#     T=input()
#     len_s=len(S)
#     len_t=len(T)
#     dp =[[0] * (len_t+1) for _ in range(len_s+1)]
#     for i in range(len_s):
#         for j in range(len_t):
#             if S[i] == T[j]:
#                 dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
#             else:
#                 dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
#     print(dp[len_s][len_t])
import sys
input = sys.stdin.readline
def solve(S,T):
    len_s=len(S)
    len_t=len(T)
    dp = [0] * (len_t+1)
    for i in range(len_s):
        mem = dp[:]
        for j in range(len_t):
            if S[i] == T[j]:
                dp[j+1] = mem[j] + 1
            elif dp[j+1] < dp[j]:
                dp[j+1] = dp[j]
    print(dp[len_t])
if __name__ == "__main__":
    N=int(input().rstrip())
    for _ in range(N):
        S=input().rstrip()
        T=input().rstrip()
        solve(S,T)