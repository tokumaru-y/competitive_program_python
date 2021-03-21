import math
N,M,K=list(map(int,input().split()))
MOD = 998244353
ans = 0
factorial_list = [1]
div_list = [1]
for i in range(1,N+1):
    factorial_list.append(factorial_list[-1] * i % MOD)
    div_list.append(pow(factorial_list[-1],MOD-2, MOD))

def nCr(n,r):
    if n < r or r < 0:
        return 0
    elif r==0:
        return 1
    return factorial_list[n]*div_list[r]*div_list[n-r]%MOD

for i in range(K+1):
    ans += M*pow(M-1,N-1-i,MOD)*nCr(N-1,i)%MOD
    ans %=MOD
print(ans)