N=int(input())
if N==1:
    print(0)
    exit()
import math
prime_list = [True] * N
prime_list[0] = False
prime_list[1] = False
for i in range(2, math.isqrt(N)+1):
    if not prime_list[i]:continue
    k = i * 2
    while k < N:
        prime_list[k] = False
        k += i
print(prime_list.count(True))