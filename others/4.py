import math
N=int(input())
ans=float("inf")
for i in range(1, math.isqrt(N)+1):
    if N%i == 0:
        ll = max(len(str(i)), len(str(N//i)))
        ans = min(ans, ll)
print(ans)