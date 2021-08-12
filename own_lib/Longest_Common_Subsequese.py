def LCM(S,T):
    """少し高速化したもの
    """
    len_s = len(S)
    len_t = len(T)
    dp=[0 for _ in range(len_t+1)]
    for i in range(len_s):
        tmp_memo = dp[:]
        for j in range(len_t):
            if S[i] == T[j]:
                dp[j+1] = tmp_memo[j]+1
            elif dp[j+1] < dp[j]:
                dp[j+1]=dp[j]
    return dp[len_t]

def LCM(S,T):
    len_s = len(S)
    len_t = len(T)
    dp = [[0] * (len_t+1) for _ in range(len_s+1)]
    for i in range(len_s):
        for j in range(len_t):
            if S[i] == T[j]:
                dp[i+1][j+1] = dp[i][j]+1
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
    return dp[len_s][len_t]
