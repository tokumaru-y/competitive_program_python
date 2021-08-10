import copy
N,W,C=list(map(int, input().split()))
Ws = [[] for _ in range(N)]
Vs = [[] for _ in range(N)]
Cs = [[] for _ in range(N)]
for i in range(N):
    w,v,s=list(map(int, input().split()))
    Ws[i]=w
    Vs[i]=v
    Cs[i]=s
dp = [[0] * (W+1) for _ in range(C+1)]
for i in range(1,51):
    _dp = [[0] * (W+1) for _ in range(C+1)]
    for x in range(C):
        _dp[x+1] = dp[x][:]
    for j in range(N):
        if Cs[j] == i:
            for x in range(1,C+1):
                for y in range(W-Ws[j], -1, -1):
                    _dp[x][y+Ws[j]] = max(_dp[x][y+Ws[j]], _dp[x][y]+Vs[j])
    for x in range(C+1):
        for y in range(W+1):
            dp[x][y]=max(dp[x][y], _dp[x][y])
print(dp[C][W])