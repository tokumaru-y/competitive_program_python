N=int(input())
if N==1:
    print(0)
elif N==2:
    print(2)
else:
    MOD=10**9+7
    ans = 10*N
    ans%=MOD
    ans-=(8*N)%MOD
    print(ans)