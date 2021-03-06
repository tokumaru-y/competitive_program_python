import math
N=int(input())
ll = set()
for i in range(2,math.isqrt(N)+1):
    tmp = i*i
    while tmp <=N:
        ll.add(tmp)
        tmp*=i
print(N-len(ll))