N=int(input())
A=list(map(int,input().split()))
ans = 0
for i in range(N-1):
    dif = A[i] - A[i+1]
    if dif >= 1:
        ans += dif
        A[i+1] += dif
print(ans)