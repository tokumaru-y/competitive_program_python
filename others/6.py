import math
N=int(input())
origin = N
sum_list = {}
for i in range(2, math.isqrt(N)+1):
    if N%i==0:
        sum_list[i]=0
        while N%i==0:
            sum_list[i]+=1
            N//=i
if N!=1 and N!=origin:
    sum_list[N] = 1
sum_n = 1
for k,v in sum_list.items():
    tmp = 0
    for t in range(v+1):
        tmp += k**t
    sum_n *= tmp
sum_n-=origin
ans = ""
if origin==sum_n:
    ans = "Perfect"
elif origin > sum_n:
    ans = "Deficient"
else:
    ans = "Abundant"
print(ans)