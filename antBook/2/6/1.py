def GCD(x, y):
    if x < y:
        x,y = y,x
    if y == 0:return x
    return GCD(y, x%y)
N=int(input())
L=list(map(int, input().split()))
res = L[0]
for i in range(1,N):
    res = GCD(res, L[i])
import math
ans = []
for n in range(1,int(math.sqrt(res))+1):
    if res % n == 0:
        ans.append(n)
        if not (n == res//n):
            ans.append(res//n)

ans.sort()
print(*ans, sep='\n')