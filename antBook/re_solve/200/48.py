N,K=list(map(int, input().split()))
CG=[list(map(int, input().split())) for _ in range(N)]
category = [[] for _ in range(11)]
values = [[] for _ in range(11)]
for c,g in CG:
    category[g].append(c)
for i in range(1,11):
    category[i] = sorted(category[i], reverse=True)
    values[i].append(0)
for i in range(1,11):
    for j in range(len(category[i])):
        values[i].append(values[i][j]+category[i][j] + j*(2))
dp=[0]*(2001)
for i in range(1,11):
    for j in range(K,-1,-1):
        for h in range(max(0, j-len(values[i])+1), j):
            dp[j] = max(dp[j], dp[h] + values[i][j-h])
print(dp[K])