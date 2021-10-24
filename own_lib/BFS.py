dx=[0,1,0,-1]
dy=[1,0,-1,0]
"""BFS ひな形
    dist: 初期頂点からの距離を格納。未訪問は-1に
    que: que。
    N: 頂点数
    graph:　隣接リスト
"""
from collections import deque
dist = [-1] * N
# スタートする頂点を0とした場合の初期化
dist[0]=0
que = deque([0])
while len(que) > 0:
    v = que.popleft()
    for nv in graph[v]:
        if dist[nv] != -1:continue
        dist[nv] = dist[v] + 1
        que.append(nv)
"""BFS 経路復元(二次元グリッドの場合)
    H,W:それぞれグリッドの高さ,幅
    dist: 初期頂点からの距離を格納。未訪問は-1に
    que: que。
    N: 頂点数
    graph:　隣接リスト
    sx,sy,gx,gy: スタートとゴール
    prev_h,prev_w: 復元用の配列
"""
from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dist = [[-1] * W for _ in range(H)]
prev_h = [[-1] * W for _ in range(H)]
prev_w = [[-1] * W for _ in range(H)]
# スタートする頂点を0とした場合の初期化
dist[sx][sy]=0
que = deque([sx,sy])
while len(que) > 0:
    _h,_w = que.popleft()
    for i in range(4):
        nh,nw = _h+dx[i], _w+dy[i]
        if not (0<=nh<H and 0<=nw<W):continue
        if grid[nh][nw] == "#":continue
        if dist[nh][nw] == -1:
            que.append([nh,nw])
            dist[nh][nw] = dist[_h][_w] + 1
            # どの頂点から来たのか。縦情報の座標をメモ
            prev_h[nh][nw] = _h
            # どの頂点から来たのか。横情報の座標をメモ
            prev_w[nh][nw] = _w
