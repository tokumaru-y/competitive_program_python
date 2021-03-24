import math
N,K=list(map(int,input().split()))
ans = 0
min_num = 0
max_num = 0
MOD = 10**9+7
for i in range(K-1):
    min_num += i
    max_num += N-i 
for i in range(K-1,N+1):
    min_num+=i
    max_num+=N-i
    ans += (max_num - min_num + 1)%MOD
    ans %= MOD
print(ans)