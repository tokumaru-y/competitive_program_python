import math
N=int(input())
is_prime = True
for i in range(2,math.isqrt(N)+1):
    if N%i==0:
        is_prime = False
        break
ans = "YES" if is_prime else "NO"
print(ans)