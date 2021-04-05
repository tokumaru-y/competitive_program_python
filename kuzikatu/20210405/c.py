import math
N=int(input())
T=[int(input()) for _ in range(N)]
ans = T[0]
def lcm(x,y):
    return (x*y)//math.gcd(x,y)
for i in range(1,N):
    ans = max(T[i], lcm(ans,T[i]))
print(ans)