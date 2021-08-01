import sys

sys.setrecursionlimit(10**5)
S=list(input().rstrip())
L = len(S)+1
dp = [[-1] * L for _ in range(L)]
def search(l,r):
    if r-l<=2:return 0
    if dp[l][r] != -1:return dp[l][r]
    res = dp[l][r]
    for m in range(l+1,r):
        res = max(res, search(l,m)+search(m,r))
        if S[l] == 'i' and S[m] == 'w' and S[r-1] == 'i':
            if search(l+1, m) == m - l - 1 and search(m+1, r-1) == r-m-2:
                res = r-l
    dp[l][r] = res
    return res
print(search(0,L-1)//3)