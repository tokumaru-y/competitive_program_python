N,D=list(map(int, input().split()))
MOD = 998244353
MAX = 510000
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
n = 2**(N)-1    
ans = (N*D%MOD)
print(ans)