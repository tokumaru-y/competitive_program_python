# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d
D,N =list(map(int, input().split()))
days = [int(input()) for _ in range(D)]
clothes = [list(map(int, input().split())) for _ in range(N)]
dp=[[-1] * N for _ in range(D+1)]
for i in range(N):
    l,r,c = clothes[i]
    if l<=days[0]<=r:
        dp[1][i] = 0
for i in range(1,D):
    temp = days[i]
    for j in range(N):
        l1,r1,c1 = clothes[j]
        if dp[i][j] < 0:continue
        for k in range(N):
            l2,r2,c2 = clothes[k]
            if not (l2<=temp<=r2):continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j]+abs(c1-c2))
print(max(dp[D]))