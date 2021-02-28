N=int(input())
A=list(map(int,input().split()))
suml = sum(A)
MOD=10**9+7
ans = 0
for i in range(N-1):
    suml -= A[i]
    ans += suml*A[i]
    ans%=MOD
print(ans)