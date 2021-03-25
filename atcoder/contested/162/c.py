import math
K=int(input())
ans = 0
def GCD(x,y):
    if y == 0:
        return x
    return GCD(y,x%y)
for i in range(1,K+1):
    for j in range(i,K+1):
        for l in range(j,K+1):
            g = math.gcd(math.gcd(i,j),l)
            ll = set([i,j,l])
            if len(ll) == 1:
                ans+=g
            elif len(ll) == 2:
                ans+=g*3
            else:
                ans+=g*6
print(ans)