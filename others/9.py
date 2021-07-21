N,M=list(map(int, input().split()))
origin = N
prime_list={}
import math
for i in range(2,math.isqrt(M)+1):
    if M%i==0:
        prime_list[i]=0
        while M%i==0:
            prime_list[i]+=1
            M//=i
if M!=1:
    prime_list[M]=1
ans = 1
MAX = 510000
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
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

# 二項係数計算
def COM(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
COMinit()
for k,v in prime_list.items():
    t = v + N - 1
    tmp = COM(t,N-1)
    ans = (tmp * ans) % MOD
print(ans)
