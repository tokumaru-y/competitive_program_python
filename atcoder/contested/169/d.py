import math
N=int(input())
ans = 0
cnt = {}
for i in range(2, math.isqrt(N)+1):
    if N%i!=0:continue
    cnt[i]=0
    while N%i==0:
        cnt[i]+=1
        N//=i
if N!=1:
    cnt[N]=1
ans = 0
for k,v in cnt.items():
    cnt = 1
    total = v
    while total >= cnt:
        ans+=1
        cnt+=1
        total-=1
print(ans)