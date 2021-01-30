import math
n=int(input())
ans=0
ll = []
tn=2*n
for i in range(1,int(math.sqrt(tn))+1):
    if tn % i == 0:
        ii = tn // i
        if (i - ii - 1) % 2 == 0:
            ans+=1
        if (ii - i - 1) % 2 == 0:
            ans+=1
print(ans) 