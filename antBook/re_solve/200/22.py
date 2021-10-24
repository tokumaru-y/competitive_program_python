import sys
input = sys.stdin.readline
def solve(S,T):
    list_s = list(S)
    list_t = list(T)
    ls = len(list_s)
    lt = len(list_t)
    dp = [[0] * (lt+1) for _ in range(ls+1)]
    for i in range(ls):
        for j in range(lt):
            if list_s[i] == list_t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
    return dp[ls][lt]
if __name__ == "__main__":
    q = int(input().rstrip())
    for _ in range(q):
        S,T=input().rstrip(),input().rstrip()
        print(solve(S,T))