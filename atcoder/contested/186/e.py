import math
t=int(input())
for _ in range(t):
    n,s,k=list(map(int,input().split()))
    d = math.gcd(n,k)
    if s % d != 0:
        print(-1)
        continue
    n //= d
    s //= d
    k //= d
    k_mod = pow(k,-1,n)
    print((-k_mod * s) % n)
