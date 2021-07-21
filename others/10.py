N,P=list(map(int, input().split()))
prime_list = {}
import math
for i in range(2, math.isqrt(P)+1):
    if P%i==0:
        prime_list[i]=0
        while P%i==0:
            prime_list[i]+=1
            P//=i
if P!=1:prime_list[P]=1
ans = 1
for k,v in prime_list.items():
    t = v//N
    ans *= k ** t if t > 0 else 1
print(ans)            