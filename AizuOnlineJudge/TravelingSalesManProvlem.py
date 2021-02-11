# 参考サイト
# https://algo-logic.info/bit-dp/#toc_id_2
# https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361#%E5%B7%A1%E5%9B%9E%E3%82%BB%E3%83%BC%E3%83%AB%E3%82%B9%E3%83%9E%E3%83%B3%E5%95%8F%E9%A1%8C
# 問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja
import sys
sys.setrecursionlimit(10000)
N,M = list(map(int,input().split()))
graph = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    s,t,d=list(map(int,input().split()))
    graph[s][t]=d
dp=[[-1] * (N) for _ in range((1<<N))]
def rec(bit,v,origin):
    if dp[bit][v]!=-1:return dp[bit][v]
    if bit == 1<<v:
        dp[bit][v]=graph[i][v]
        return dp[bit][v]
    res = float('inf')
    pre_bit = (bit ^ (1<<v))
    for u in range(N):
        if not (pre_bit & 1<<u):continue
        num = rec(pre_bit,u,origin) + graph[u][v]
        if res > num:
            res = num
    dp[bit][v]=res
    return dp[bit][v]

ans = float('inf')
for i in range(N):
    ans = min(rec((1<<N)-1,i,i),ans)
print(ans if ans != float('inf') else -1)