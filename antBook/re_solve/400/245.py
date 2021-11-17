# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c
N,K,S=list(map(int, input().split()))
ans = []
if N == K:
    ans = [S for _ in range(N)]
elif S == 1:
    ans = [1 for _ in range(K)]
    for _ in range(N-K):
        ans.append(10**9)
else:
    if K == N-1:
        ans = [1 if i%2==0 else S-1 for i in range(N)]
    else:
        ans = [1 if i%2==0 else S-1 for i in range(K+1)]
        t = 10**9 if S < 10**9 else 2
        for i in range(N-(K+1)):
            ans.append(t)
print(*ans, sep=" ")