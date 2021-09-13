# https://atcoder.jp/contests/abc052/tasks/arc067_a
import math
from collections import defaultdict

def prime_factorize(num, dict=None):
    """numを素因数分解する"""
    import math
    dict = {} if dict is None else dict
    origin = num
    for i in range(2, int(math.sqrt(origin))+1):
        if num%i==0:
            while num%i==0:
                dict[i]+=1
                num//=i
    if num != 1:
        dict[num] +=1
    return dict
ans = 1
N=int(input())
MOD = 10**9+7
dict = defaultdict(int)
for i in range(2, N+1):
    dict = prime_factorize(i,dict)
for num, cnt in dict.items():
    ans *= cnt+1
    ans %= MOD
print(ans)