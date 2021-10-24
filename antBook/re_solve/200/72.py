MAX = 2*10**5
MOD=10**9+7
fac=[0] * MAX
finv=[0]* MAX
inv=[0] * MAX
# テーブルの初期化
def COMinit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;

# 二項係数計算
def COM(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
import math
N,M=list(map(int, input().split()))
abs_N=abs(N)
if abs_N == 1:
    print(1)
    exit()
COMinit()
prime_list = {}
for i in range(2, math.isqrt(abs_N)+1):
    if abs_N%i==0:
        prime_list[i]=0
        while abs_N%i==0:
            prime_list[i]+=1
            abs_N//=i
if abs_N != 1:
    prime_list[abs_N] = 1
ans = 1
for count in prime_list.values():
    ans *= COM(M+count-1, M-1)
    ans %= MOD
for _ in range(M-1):
    ans *= 2
    ans %= MOD
print(ans)