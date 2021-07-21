import math
N=int(input())
ans = ["{}:".format(N)]
for i in range(2,int(math.sqrt(N))+1):
    if N%i == 0:
        while N%i==0:
            N//=i
            ans.append(str(i))
if N!=1:
    ans.append(str(N))
print(" ".join(ans))