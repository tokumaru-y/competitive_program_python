"""DFSのテンプレート実装
    N: 頂点数
    seen (list): i番目の頂点に訪れたかseen[i]=Trueは来訪済み
    grash (list): 隣接リスト形式のグラフ情報
"""
import sys
sys.setrecursionlimit(10**9)
seen = [False] * N
def dfs(graph, v):
    seen[v]=True

    for next_v in graph[v]:
        if seen[next_v]:continue
        dfs(graph, next_v)

"""DFS
   first_order: 行きがけ順 i番目の頂点が何番目に入ったか
   last_order: 帰りがけ順 i番目の頂点が何番目に再帰関数を抜けたか
   last_order_num はglobalを用いて使用
"""
import sys
sys.setrecursionlimit(10**9)
seen = [False] * N
first_order = [0] * N
last_order = [0] * N
last_order_num = 0
def dfs(graph, v, first_order_num):
    global last_order_num
    first_order[v] = first_order_num
    first_order_num += 1

    seen[v]=True

    for next_v in graph[v]:
        if seen[next_v]:continue
        dfs(graph, next_v, first_order_num)
    
    last_order[v]=last_order_num
    last_order_num += 1