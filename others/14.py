N=int(input())
origin = N
prime_table = {}
import math
for i in range(2,math.isqrt(N)+1):
    if N%i==0:
        prime_table[i]=0
        while N%i==0:
            prime_table[i]+=1
            N//=i
if N!=1:
    prime_table[N]=1
sum_n=1
for k,v in prime_table.items():
    tmp = 0
    for t in range(v+1):
        tmp += k**t
    sum_n*=tmp
sum_n-=origin
if sum_n == origin:
    print("Perfect")
elif sum_n < origin:
    print("Deficient")
else:
    print("Abundant")