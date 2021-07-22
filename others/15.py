N=int(input())
ans = 0
import math
for i in range(1,N+1,2):
    target = i
    prime_table = {}
    for j in range(2, math.isqrt(i)+1):
        if target%j==0:
            prime_table[j]=0
            while target%j==0:
                prime_table[j]+=1
                target//=j
    if target!=1:
        prime_table[target]=1
    cnt = 1
    for k,v in prime_table.items():
        cnt *= v+1
    if cnt == 8:ans+=1
print(ans)