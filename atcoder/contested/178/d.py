import math
S=int(input())
digit = S//3
MOD=10**9+7
ans=0
if S<=2:
    print(0)
else:
    for d in reversed(range(1,digit+1)):
        if d==1:
            ans+=1
            ans%=MOD
            continue
        left = S - 3*d
        if left == 0:
            ans+=1
            continue
        plus = math.factorial(left+d-1)//(math.factorial(left)*math.factorial(d-1))
        plus%=MOD
        ans+=plus
        ans%=MOD
    print(ans)