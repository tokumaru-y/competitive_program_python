N,M=list(map(int, input().split()))
origin = M
prime_table=[]
import math
for i in range(2,math.isqrt(M)+1):
    if M%i==0:
        prime_table.append(i)
        if i != M//i:
            prime_table.append(M//i)
if M!=1:prime_table.append(M)
prime_table.sort(reverse=True)
ans = 1
for prime in prime_table:
    if N*prime <= origin:
        print(prime)
        exit()
print(ans)