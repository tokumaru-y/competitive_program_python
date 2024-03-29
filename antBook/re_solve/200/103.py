# https://atcoder.jp/contests/abc110/tasks/abc110_d
from collections import defaultdict
def prime_factorize(num, dict=None):
    """numを素因数分解する"""
    import math
    dict = {} if dict is None else dict
    origin = num
    for i in range(2, int(math.sqrt(origin))+1):
        if num%i==0:
            while num%i==0:
                dict[i]+=1
                num//=i
    if num != 1:
        dict[num] +=1
    return dict
MAX = 510000
MOD=10**9+7
fac=[0] * MAX
finv=[0]* MAX
inv=[0] * MAX
# テーブルの初期化
def COMinit():
    """
    nCk = n! * k!**-1 * ((n-k)!)**-1を考える
    fac:= 上記のn!の部分
    finv:= 上記のN**-1と逆数になっている部分
    inv:= finvを計算するための1,2,...nの逆元をinv[1],inv[2],...inv[n]
    """
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

# 二項係数計算
def COM(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

N,M=list(map(int, input().split()))
prime_dict = prime_factorize(M, defaultdict(int))
COMinit()
ans = 1
for cnt in prime_dict.values():
    ans *= COM(cnt+N-1, N-1)
    ans %= MOD
print(ans)