# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2502
N=int(input())
dp=[0] * (394)
SLP=[list(map(int, input().split())) for _ in range(N)]
for s,l,p in SLP:
    for j in range(394):
        for k in range(s,l+1):
            if 0<=j+k<=393:
                dp[j+k] = max(dp[j+k], dp[j]+p)
M=int(input())
ans = []
for _ in range(M):
    w=int(input())
    if dp[w] == 0:
        print(-1)
        exit()
    else:
        ans.append(dp[w])
print(*ans, sep="\n")