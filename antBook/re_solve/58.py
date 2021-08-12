def LCM(S,T):
    len_s = len(S)
    len_t = len(T)
    dp = [[float("inf")] * (len_t+1) for _ in range(len_s+1)]
    dp[0][0]=0
    for i in range(len_s):
        for j in range(len_t):
            if S[i] == T[j]:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
            dp[i+1][j+1]=min(dp[i+1][j+1], dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+1)
    return dp[len_s][len_t]



if __name__ == "__main__":
    S=input()
    T=input()
    print(LCM(S,T))