# 参考サイト
# https://algo-logic.info/bit-dp/#toc_id_2
# https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361#%E5%B7%A1%E5%9B%9E%E3%82%BB%E3%83%BC%E3%83%AB%E3%82%B9%E3%83%9E%E3%83%B3%E5%95%8F%E9%A1%8C
# 問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja

# 参考の提出
# http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3144506
# https://dalekspritner.hatenablog.com/entry/2018/09/27/231030
import sys
sys.setrecursionlimit(10000)
N,M = list(map(int,input().split()))
graph = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    s,t,d=list(map(int,input().split()))
    graph[s][t]=d
dp=[[-1] * (N) for _ in range((1<<N))]

def rec(bit,v):
    if dp[bit][v]>0:return dp[bit][v]

    if bit == (1<<N)-1 and v==0:
        dp[bit][v] = 0
        return 0
    ans = float('inf')
    for u in range(N):
        if not (bit >> u & 1):
            ans = min(ans, rec(bit|1<<u, u) + graph[v][u])
    dp[bit][v]=ans
    return ans

ans = rec(0,0)
print(ans if ans != float('inf') else -1)