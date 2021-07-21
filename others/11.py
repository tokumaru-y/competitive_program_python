A,B=list(map(int, input().split()))
def GCD(x,y):
    if x<y:x,y=y,x
    if y == 0:
        return x
    return GCD(y,x%y)
G = GCD(A,B)
import math
prime_cnt = 0
for i in range(2,math.isqrt(G)+1):
    if G%i==0:
        prime_cnt+=1
        while G%i==0:
            G//=i
if G!=1:
    prime_cnt+=1
ans = prime_cnt+1
print(ans)