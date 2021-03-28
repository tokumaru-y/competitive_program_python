N=int(input())
A=list(map(int,input().split()))
ans = float('inf')
for i in range(1<<(N-1)):
    ord = 0
    xord = 0
    for j in range(N+1):
        if j<N:ord |= A[j]
        if j==N or (i & 1<<j):
            xord ^= ord
            ord = 0
    ans = min(ans, xord)
print(ans)