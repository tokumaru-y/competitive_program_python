import math
N=int(input())
ans=[]
for i in range(1,math.isqrt(N)+1):
    if N%i==0:
        ans.append(i)
        if N//i!=i:
            ans.append(N//i)
ans.sort()
print(*ans,sep='\n')