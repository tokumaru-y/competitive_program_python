N=int(input())
P=list(map(int, input().split()))
dp=[0] * (100*100+1)
dp[0] = 1
for i in range(N):
    p=P[i]
    for j in reversed(range(100*100+1)):
        if j-p >= 0 and dp[j-p] > 0:
            dp[j] = 1
print(sum(dp))