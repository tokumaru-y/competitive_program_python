S=list(input())
if len(list(set(S))) > 5:
    print(-1)
    exit()
S.reverse()
primes = [1,3,5,7,9]
import math
from itertools import permutations
table = {}
for i in range(len(S)):
    if S[i] in table:
        table[S[i]].append(i)
    else:
        table[S[i]] = [i]
def is_prime(num):
    if num == 1:return False
    for i in range(2, math.isqrt(num)+1):
        if num%i==0:
            return False
    return True
for item in permutations(primes):
    num = 0
    ind = 0
    for k,vv in table.items():
        for v in vv:
            num += 10**v*item[ind]
        ind+=1
    if is_prime(num):
        print(num)
        exit()
print(-1)