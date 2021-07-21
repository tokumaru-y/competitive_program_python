import math
N=int(input())
origin = N
ans = 1
sum_list = [0]*(N+1)
for n in range(2, N+1):
    for i in range(2, math.isqrt(n)+1):
        if n%i==0:
            while n%i==0:
                sum_list[i] += 1
                n//=i
    if n!=1:
        sum_list[n]+=1
for v in sum_list:
    ans *= v+1
    ans %= 10**9+7
print(ans)