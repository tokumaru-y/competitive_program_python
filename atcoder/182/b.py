import math
N=int(input())
A=list(map(int,input().split()))
cnt = {}
def divisor(n):
    res = []
    for i in range(1,math.isqrt(n)+1):
        if n%i==0:
            if i in cnt:
                cnt[i]+=1
            else:
                cnt[i]=1
            if n//i != i:
                if n//i in cnt:
                    cnt[n//i]+=1
                else:
                    cnt[n//i]=1
for a in A:
    divisor(a)
ans=0
tmpcnt=0
cnt[1]=0
for k,v in cnt.items():
    if tmpcnt < v:
        ans=k
        tmpcnt=v
print(ans)
