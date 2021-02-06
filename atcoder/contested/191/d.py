import math,decimal
x,y,r=list(map(lambda x : int(decimal.Decimal(x)*10000),input().split()))
ans=0
s=x-r
e=x+r
for i in range(-2*10**5,2*10**5+1):
    i*=10000
    tmp = r**2 - (x-i)**2
    if tmp >= 0:
        tmp = math.isqrt(tmp)
        low = -(-(y-tmp)//10000)
        high = (y+tmp)//10000
        ans += high - low + 1
print(ans)