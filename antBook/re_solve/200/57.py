def LCM(S,T):
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


if __name__ == "__main__":
    N=int(input())
    for _ in range(N):
        S=input().strip()
        T=input().strip()
        print(LCM(S,T))
