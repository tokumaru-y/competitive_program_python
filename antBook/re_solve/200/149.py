# https://atcoder.jp/contests/abc007/tasks/abc007_4
A,B=list(map(int, input().split()))
def solve(S):
    S = str(S)
    len_s = len(S)
    # dp[i][j][k]:=jが1の時、未満フラグが立っている
    dp = [[[0] * 2 for _ in range(2)] for _ in range(len_s+1)]
    dp[0][0][0]=1
    for i in range(len_s):
        target = int(S[i])
        d_range = [target+1, 10]
        for j in range(2):
            for k in range(2):
                for d in range(d_range[j]):
                    dp[i+1][j or (d<target)][k or d==4 or d== 9] += dp[i][j][k]
    return dp[len_s][1][1] + dp[len_s][0][1]

ans = solve(B) - solve(A-1)
print(ans)