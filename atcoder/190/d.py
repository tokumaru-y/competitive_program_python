import math
N=int(input())
ans = 0 
target=4*N
for i in range(1,math.isqrt(target)+1):
    if target % i == 0:
        if ((target//i) + i) % 2 == 1:
            ans+=2
print(ans)