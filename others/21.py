from collections import defaultdict
import math
N=int(input())
table = defaultdict(int)
for i in range(1,N+1):
    target = i
    for j in range(2, math.isqrt(i)+1):
        if target%j==0:
            while target%j==0:
                table[j]+=1
                target//=j
    if target != 1:table[target]+=1
count = {75: 0, 25: 0, 15: 0, 5: 0, 3: 0}
for k,v in table.items():
    if v >= 74:
        count[75]+=1
    if v >= 24:
        count[25]+=1
    if v >= 14:
        count[15]+=1
    if v >= 4:
        count[5]+=1
    if v >= 2:
        count[3]+=1
ans = count[75] + (count[25] * (count[3] - 1)) + count[15] * (count[5]-1)+ count[5] * (count[5]-1) * (count[3]-2)//2
print(ans)