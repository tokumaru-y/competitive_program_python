D,N=list(map(int, input().split()))
Ds=[int(input()) for _ in range(D)]
ABC=[list(map(int, input().split())) for _ in range(N)]
dp = [[float("-inf")] * N for _ in range(D+1)]
for n in range(N):
    a,b,c=ABC[n]
    if not a<=Ds[0]<=b:continue
    dp[0][n]=0
for i in range(1,D):
    for j in range(N):
        a,b,c=ABC[j]
        if not a<=Ds[i]<=b:continue
        for n in range(N):
            dp[i][j] = max(dp[i][j], dp[i-1][n] + abs(c-ABC[n][2]))
print(max(dp[D-1]))