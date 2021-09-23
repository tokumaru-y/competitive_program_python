# https://atcoder.jp/contests/abc017/tasks/abc017_4
N,M=list(map(int, input().split()))
F=[int(input()) for _ in range(N)]
L=[0] * (N+1)
left = 0
cnt_table = [0] * (10**5+1)
for right in range(N):
    cnt_table[F[right]]+=1
    while left < right and cnt_table[F[right]] > 1:
        cnt_table[F[left]] -= 1
        left += 1
    L[right+1] = left
dp=[0] * (N+1)
dp[0] = 1
sum = [0] * (N+2)
sum[1]=1
MOD = 10**9+7
for i in range(1,N+1):
    dp[i] = (sum[i] - sum[L[i]] + MOD)%MOD
    sum[i+1] = (sum[i] + dp[i])%MOD
print(dp[N])