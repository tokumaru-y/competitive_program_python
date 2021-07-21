import math
N=int(input())
ans=float("inf")
for i in range(1, math.isqrt(N)+1):
    if N%i == 0:
        ans = min(ans, len(str(max(i,N//i))))
print(ans)