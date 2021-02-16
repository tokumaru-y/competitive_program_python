from collections import deque
N,M=list(map(int,input().split()))
AB=[list(map(lambda x : int(x)-1,input().split())) for _ in range(M)]
K=int(input())
C=list(map(lambda x : int(x)-1,input().split()))
edge = [[] for _ in range(N)]
for a,b in AB:
    edge[a].append(b)
    edge[b].append(a)

def bfs(c):
    tmp = [float('inf')] * N
    tmp[c]=0
    q = deque([c])
    while len(q) > 0:
        n = q.popleft()
        if edge[n]:
            for e in edge[n]:
                if tmp[e] == float('inf'):
                    tmp[e] = tmp[n] + 1
                    q.append(e)
    return [tmp[c] for c in C]

cost = [bfs(c) for c in C]
dp = [[float('inf')] * K for _ in range(1<<K)]
for i in range(K):
    dp[1<<i][i] = 1
for bit in range(1<<K):
    for i in range(K):
        # if dp[bit][i] == float('inf'):continue
        for j in range(K):
            if bit & 1<<j:continue
            if dp[bit ^ 1<<j][j] > dp[bit][i] + cost[i][j]:
                dp[bit ^ 1<<j][j] = dp[bit][i] + cost[i][j]

ans = min(dp[-1])
print(ans if ans != float('inf') else -1)