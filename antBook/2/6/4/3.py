# MAX_LEN = 999999+1
# prime_list = [True] * MAX_LEN
# prime_list[0] = False
# prime_list[1] = False
# import math
# prime_count = [0] *(MAX_LEN)
# for i in range(2, int(math.sqrt(MAX_LEN))+1):
#     prime_count[i] = prime_count[i-1]
#     if not prime_list[i]:continue
#     prime_count[i]+=1
#     k = i + i
#     while k <= MAX_LEN:
#         prime_list[k] = False
#         k += i
# while True:
#     try:
#         n=int(input())
#     except:
#         break
#     print(prime_count[n])
MAX_LEN = 999999+1
prime_list = [True] * MAX_LEN
prime_list[0] = False
prime_list[1] = False
import math
primes = []
for i in range(2, MAX_LEN):
    if not prime_list[i]:continue
    primes.append(i)
    k = i+i
    while k< MAX_LEN:
        prime_list[k]=False
        k+=i
from bisect import bisect_right
while True:
    try:
        n=int(input())
        print(bisect_right(primes, n))
    except:
        break