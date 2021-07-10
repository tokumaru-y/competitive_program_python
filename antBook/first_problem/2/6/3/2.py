import math
N=int(input())
cnt = [0] * (10**3+1)
for n in range(1, N+1):
    for i in range(2, math.isqrt(n)+1):
        while n%i==0:
            cnt[i] += 1
            n//=i
    if n!=1:cnt[n]+=1
ans = 1
for i in range(2,N+1):
    ans *= cnt[i]+1 if cnt[i] > 0 else 1
    ans %= 10**9+7
print(ans)