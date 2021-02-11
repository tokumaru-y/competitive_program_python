# 参考サイト
# https://algo-logic.info/bit-dp/#toc_id_2
# https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361#%E5%B7%A1%E5%9B%9E%E3%82%BB%E3%83%BC%E3%83%AB%E3%82%B9%E3%83%9E%E3%83%B3%E5%95%8F%E9%A1%8C
# 問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja
import sys
sys.setrecursionlimit(10000)
V,E = list(map(int,input().split()))
graph = [[float('inf')] * V for _ in range(V)]
for _ in range(E):
    s,t,d=list(map(int,input().split()))
    graph[s][t]=d
dp=[[0] * (V) for _ in range((1<<V))]
def rec(bit,v):
    if (dp[bit][v] != -1):return dp[bit][v]
    if bit == (1<<v):
        dp[bit][v] = 0
        return dp[bit][v]
    res = float('inf')
    prev_bit = (bit^(1<<v))
    for i in range(V):
        if not(prev_bit & (1<<i)): continue
        num = (rec(prev_bit,i) + graph[i][v])
        if res > num:
            res = num
    dp[bit][v] = res
    return dp[bit][v]
ans=float('inf')
for i in range(V):
    ans = rec((1<<V)-1,i)
print(ans if ans!=float('inf') else -1)
