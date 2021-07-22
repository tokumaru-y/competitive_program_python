N=int(input())
count_list = {}
import math
for i in range(2, math.isqrt(N)+1):
    if N%i==0:
        count_list[i]=0
        while N%i==0:
            count_list[i]+=1
            N//=i
if N!=1:count_list[N]=1
ans = 0
for k,v in count_list.items():
    need = 1
    tmp = 0
    left = v
    while need<=left:
        tmp+=1
        left -= need
        need+=1
    ans += tmp
print(ans)