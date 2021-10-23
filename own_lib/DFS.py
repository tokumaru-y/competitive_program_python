
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
    seen (list): i番目の頂点に訪れたかseen[i]=Trueは来訪済み
    grash (list): 隣接リスト形式のグラフ情報
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
"""DFS 二部グラフ
    grash (list): 隣接リスト形式のグラフ情報
    color: 1,0で色を判別。-1は未訪問
    Returns:
        boolean:二部グラフなのか
"""
color = [-1] * N
def dfs_bipartite(graph, v, c):
    color[v] = c
    for next_v in graph[v]:
        if color[next_v] != -1:
            if color[next_v] == c:return False
            continue
        if not dfs_bipartite(graph, v, 1-c):return False
    return True

"""DFS 根のない木の走査
    depth:　木の深さ
    sub_tree_size: 自身も含めた部分木のサイズ
    Attentions:
        木の特徴を生かして、これまで到達したかのフラグはp(parent)を見て判断。
"""
depth = [0] * N
sub_tree_size = [0] * N
def dfs_tree(graph, v, p, d):
    depth[v] = d
    for nv in graph[v]:
        if nv == p:continue
        dfs(graph, nv, v, d+1)
    
    # 部分木のサイズ
    sub_tree_size[v]=1
    for c in graph[v]:
        if c == p:continue
        sub_tree_size[v] += sub_tree_size[c]

"""DFS トポロジカルソート
    order: トポロジカルソート結果を格納する配列
"""
order = []
seen = [False] * N
def dfs_toporo(graph, v):
    seen[v] = True
    for nv in graph[v]:
        if seen[nv]:continue
        dfs_toporo(graph, nv)
    order.append(v)
order.reverse()

"""DFS サイクル検出
    seen: 訪問済みか
    finish: 帰りがけですでに訪れたか(dfsを一度抜けたか)
    pos: サイクル中の頂点番号
    cycle:サイクルの頂点
"""
from collections import deque
pos = -1
seen = [False] * N
finish = [False] * N    
history = deque([])
def dfs_cycle(v, p):
    global pos
    seen[v] = True
    history.append(v)
    for nv in graph[v]:
        if nv == p:continue
        if finish[nv]:continue
        # サイクル検出
        if seen[nv] and not finish[nv]:
            pos = nv
            return
        dfs_cycle(nv, v)
        if pos != -1:
            return
    history.pop()
    finish[v]=True
cycle = []
while len(history) > 0:
    t = history.pop()
    cycle.append(t)
    if t == pos:break
cycle = list(set(list))
"""DFS 強連結成分分解 https://manabitimes.jp/math/1250
"""
To Be Continued...