# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=jp
from copy import deepcopy
V,E=list(map(int, input().split()))
graph = [[float("inf")] * V for _ in range(V)]
for _ in range(E):
    s,t,d = list(map(int, input().split()))
    s-=1
    t-=1
    graph[s][t]=d
dp = [[float("inf")] * V for _ in range(1<<V)]
for i in range(V):
    dp[0][i]=0
    dp[1<<i][1]=0
ans = float("inf")
def set_dp(tmp_dp, s):
    for bit in range(1<<V):
        for i in range(V):
            if bit & (1<<i):
                for j in range(V):
                    if i == j or not(bit & 1<<j) or graph[j][i] == float("inf"):continue
                    tmp_dp[bit][i] = min(tmp_dp[bit][i], tmp_dp[bit^(1<<i)][j] + graph[j][i])
    return tmp_dp
for start in range(V):
    tmp_dp = deepcopy(dp)
    tmp_dp = set_dp(tmp_dp,start)
    tmp_ans = float("inf")
    for i in range(V):
        tmp_ans = min(tmp_ans, tmp_dp[(1<<V)-1][i] + graph[i][start])
    ans = min(ans, tmp_ans)
print(ans if ans < float("inf") else -1)