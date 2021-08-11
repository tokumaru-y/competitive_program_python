D,N=list(map(int, input().split()))
day = [int(input()) for _ in range(D)]
ABC=[list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(D)]
for i in range(D):
    for j in range(N):
        if ABC[j][0] <= day[i] <= ABC[j][1]:
            if i == 0:
                dp[i][j]=0
            else:
                for k in range(N):
                    if dp[i-1][k] >= 0:
                        dp[i][j]=max(dp[i][j], dp[i-1][k] + abs(ABC[k][2] - ABC[j][2]))
ans = max(dp[D-1])
print(ans)