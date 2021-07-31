# N,Z,W=list(map(int, input().split()))
# A=list(map(int, input().split()))
# # dp[i][j]:= 山札からi枚取り除いたときの絶対値(jはAさんかどうか)
# dp = [[True, False] for _ in range(N+1)]
# dp[0]=abs(Z-W)
# def dfs(dp, time):
#     pass
# dfs(dp, 0)
# print(dp[N])