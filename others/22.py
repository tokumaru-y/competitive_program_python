import math
from collections import defaultdict
A,B=list(map(int, input().split()))
dif = A-B
prime_count = defaultdict(int)
for i in range(B+1, A+1):
    target = i
    for j in range(2, math.isqrt(i)+1):
        if i%j==0:
            while target%j==0:
                prime_count[j]+=1
                target//=j
    if target!=1:prime_count[target]+=1
ans = 1
MOD = 10**9+7
for k,v in prime_count.items():
    ans *= (v+1)
    ans %= MOD
print(ans)
# import math
# from collections import defaultdict
# A,B=list(map(int, input().split()))
# table=defaultdict(int)
# origin=A
# for i in range(2, math.isqrt(A)+1):
#     if origin%i==0:
#         while origin%i==0:
#             table[i]+=1
#             origin//=i
# if origin!=1:table[origin]+=1
# origin_b = B
# for i in range(2, math.isqrt(B)+1):
#     if origin_b%i==0:
#         while origin_b%i==0:
#             table[i]-=1
#             origin_b//=i
# if origin_b!=1:table[origin_b]-=1
# ans = 1
# MOD = 10**9+7
# print(table)
# for k,v in table.items():
#     ans *= v
#     ans %= MOD
# print(ans)