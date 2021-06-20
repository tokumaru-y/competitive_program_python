import math
N,M=list(map(int, input().split()))
LEN = 210000
fac = [0] * LEN
finv = [0] * LEN
inv = [0] * LEN
MOD = 10**9+7

def com_tabel_init(MOD, LEN):
    """
    nCmので使用
    あらかじめテーブルを初期化しておくこと
    fac: fac[a]=a! 累乗計算結果
    finv: finv[a]=(a**-1)!
    inv: finvで使用する
    """
    fac[0], fac[1] =1 ,1
    finv[0], finv[1] = 1, 1
    inv[1]=1
    for i in range(2, LEN):
        fac[i] = fac[i-1]*i%MOD
        inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
        finv[i] = finv[i-1] *inv[i] % MOD

def nCm(n, m, MOD):
    if n<m:return 0
    if n < 0 or m < 0:return 0
    return fac[n] * (finv[m] * finv[n-m] % MOD) % MOD

prime_cnt = {}
m = M
for num in range(2, int(math.sqrt(m))+1):
    tmp_cnt = 0
    while M%num == 0:
        tmp_cnt+=1
        M//=num 
    prime_cnt[num] = tmp_cnt
if M != 1:prime_cnt[M]=1
ans = 1
com_tabel_init(MOD, LEN)
for p, cnt in prime_cnt.items():
    ans *= nCm(cnt+N-1, N-1, MOD)
    ans %= MOD
print(ans)