import math
N=int(input())
L=list(map(int, input().split()))
ans = []
def GCD(x,y):
    if x<y:x,y=y,x
    if y==0:return x
    return GCD(y,x%y)
m=L[0]
for i in range(1,N):
    m=GCD(m,L[i])
for i in range(1,int(math.sqrt(m))+1):
    if m%i==0:
        ans.append(i)
        if m//i != i:ans.append(m//i)
ans.sort()
print(*ans, sep="\n")