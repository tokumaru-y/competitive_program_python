N=int(input())
origin = N
sum_list={}
import math
for i in range(2,int(math.sqrt(N))+1):
    if N%i==0:
        sum_list[i] = 0
        while N%i==0:
            sum_list[i]+=1
            N//=i
if N!=1:
    sum_list[N]=1
ans = origin
for k,v in sum_list.items():
    ans *= (1-(1/k))
print(int(ans))