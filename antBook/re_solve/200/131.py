# https://atcoder.jp/contests/abc017/tasks/abc017_4
N,M=list(map(int, input().split()))
F=[int(input()) for _ in range(N)]
MOD = 10**9+7
used=[False] * (10**5+1)
right = 0
ans = 0
for left in range(N):
    while right < N and not used[F[right]]:
        used[F[right]] = True
        right += 1
    ans += right - left
    ans %= MOD
    if right == left:
        right += 1
    else:
        used[F[left]]=False
print(ans%MOD)