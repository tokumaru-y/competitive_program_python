N,K=list(map(int, input().split()))
A=list(map(int, input().split()))
dp=[False]*(K+1)
for i in range(1,K+1):
    for a in A:
        nx = i - a
        if nx>=0:
            dp[i]|= not dp[nx]
print("First" if dp[K] else "Second")
