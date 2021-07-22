from collections import defaultdict
import math


N=int(input())
prime_counter = defaultdict(int)
origin = N
for i in range(2, int(math.sqrt(N))+1):
    if origin%i==0:
        while origin%i==0:
            prime_counter[i]+=1
            origin//=i
if origin!=1:prime_counter[origin]+=1
min_ans = len(prime_counter)
max_ans = 1
for k,v in prime_counter.items():
    max_ans *= (v+1)
max_ans -= 1
print(min_ans, max_ans)