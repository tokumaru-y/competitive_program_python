N,K=list(map(int, input().split()))
A=[int(input()) for _ in range(N)]
sum_count = [0] * (N)
for i in range(N):
    sum_count[i]= sum_count[i-1]+A[i]
dp = [[float("inf")] * (N+1) for _ in range(N+1)]
dp[0][0]=0
dp[1][0]=0
dp[1][1]=1
import math
for i in range(1,N):
    for j in range(i+1):
        if dp[i][j] != float("inf"):
            tmp = dp[i][j]*A[i]
            need = (tmp//sum_count[i-1])+1
            if need+dp[i][j] < sum_count[i]:dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+need)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
if sum_count[N-1] == K:
    print(1)
    exit()

for i in reversed(range(N+1)):
    if dp[N][i] <= K:
        print(i)
        exit()