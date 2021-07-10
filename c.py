N=int(input())
C=list(map(int, input().split()))
MOD=10**9+7
ans = 1
C.append(0)
C.sort()
left = 0
for i in range(1,N+1):
    left+=C[i]-C[i-1]
    ans *= left
    left -=1
    ans%=MOD
print(ans)
