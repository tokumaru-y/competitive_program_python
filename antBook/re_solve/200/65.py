from bisect import bisect_left
N=int(input())
A=list(map(int,  input().split()))
dp = [float("inf")] * (N+1)
dp[0]=0
for i in range(N):
    a=A[i]
    ind = bisect_left(dp,a)
    dp[ind]=a
for i in reversed(range(N+1)):
    if dp[i] != float("inf"):
        print(i)
        exit()
        