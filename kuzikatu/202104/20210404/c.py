import math
N=int(input())
A=list(map(int ,input().split()))
prime=[True]*(51)
prime[0]=False
prime[1]=False
for i in range(2,51):
    if prime[i]:
        tmp = i + i
        while tmp<=50:
            prime[tmp]=False
            tmp+=i
num=[]
for i in range(51):
    if prime[i]:num.append(i)
ans = float('inf')
for bit in range(1,1<<len(num)):
    tmp = 1
    for i in range(len(num)):
        if bit & 1<<i:
            tmp*=num[i]
    flag = True
    for a in A:
        g = math.gcd(a,tmp)
        if g==1:
            flag=False
    if flag:
        ans = min(ans, tmp)
print(ans)