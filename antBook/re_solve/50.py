# TODO: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2895
MOD = 10**9+7
S=list(input())
T=list(reversed(S))
n = len(S)
# res[i][c]:=i文字目以降で最初に文字cが登場するindex(存在しないときはn)
def calc_next(s):
    n = len(s)
    res = [[n] * 26 for _ in range(n+1)] 
    for i in range(n-1,-1,-1):
        for j in range(26):
            res[i][j] = res[i+1][j]
        res[i][ord(s[i])-97] = i
    return res
ns = calc_next(S)
nt = calc_next(T)
dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        for k in range(26):
            ni = ns[i][k]
            nj = nt[j][k]
            if ni+nj+2>n:continue
            dp[ni+1][nj+1]+= dp[i][j]
            dp[ni+1][nj+1]%=MOD
ans = 0
for i in range(n+1):
    for j in range(n-i+1):
        num = 1
        for k in range(26):
            if ns[i][k]+1+j<=n:num+=1
        ans = (ans + (dp[i][j] * num)% MOD) % MOD
print(ans-1)