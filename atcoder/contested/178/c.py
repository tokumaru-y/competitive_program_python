N=int(input())
if N==1:
    print(0)
elif N==2:
    print(2)
else:
    MOD=10**9+7
    div = (9**N)%MOD+(9**N)%MOD-(8**N)%MOD
    ans = (10**N)%MOD - div
    print(ans%MOD)