prime_list = [True] * (10**5+1)
prime_list[0]=False
prime_list[1]=False
import math
for n in range(2,math.isqrt(10**5)+1):
    if not prime_list[n]:continue
    k = n + n
    while k <= 10**5:
        prime_list[k]=False
        k+=n
prime_count = [0] * (10**5+1)
for n in range(2, 10**5+1):
    if prime_list[(n+1)//2] and prime_list[n]:
        prime_count[n] = prime_count[n-1]+1
    else:
        prime_count[n] = prime_count[n-1]

Q = int(input())
for _ in range(Q):
    a,b = list(map(int, input().split()))
    cnt = prime_count[b] - prime_count[a-1]
    print(cnt)
