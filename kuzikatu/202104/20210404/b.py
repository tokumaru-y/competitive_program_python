N=int(input())
A=list(map(int,input().split()))
B=list(map(int, input().split()))
suma = [0]*(N+1)
sumb = [0]*(N+1)
for i in range(N):
    suma[i+1] = suma[i] + A[i]
    sumb[i+1] = sumb[i] + B[i]
ans = 0
for i in range(1,N+1):
    tmpa = suma[i]
    tmpb = sumb[-1] - sumb[i-1]
    ans = max(ans, tmpa+tmpb)
print(ans)