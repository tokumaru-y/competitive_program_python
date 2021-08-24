class UF:
    """Union Find
    UF(x):
    self.par:　各頂点の親を表す
    self.deepth: 頂点の深さ表す
    """
    def __init__(self, x):
        """[summary]

        Args:
            x (int): 頂点数
        """
        self.par = [i for i in range(x)]
        self.deepth = [1 for _ in range(x)]
    
    def root(self, x):
        """[summary]

        Args:
            x ([int]): 探索対象の頂点

        Returns:
            int: 頂点の親頂点
        """
        if x == self.par[x]: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def same(self, x, y):
        """[summary]

        Args:
            x ([int]): 頂点
            y ([int]): 頂点

        Returns:
            boolean: x,yが同じグループに属しているか
        """
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry
    
    def unite(self, x, y):
        """[summary]

        Args:
            x ([int]): 頂点
            y ([int]): 頂点

        Returns:
            boolean:
            　True: 各頂点が違う親で結びつけられた
            　False: 各頂点が同じ親だった
        """
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:return False
        if self.deepth[rx] > self.deepth[ry]: rx, ry = ry, rx
        self.deepth[ry] += self.deepth[rx]
        self.par[rx] = self.par[ry]
        return True
from heapq import heappop,heapify
N,M=list(map(int, input().split()))
weight = [[float("inf")] * N for _ in range(N)]
for _ in range(M):
    s,t,w = list(map(int, input().split()))
    weight[s][t] = w
    weight[t][s] = w
Q=int(input())
tops=[]
used_edges = []
used=[False]*N
for _ in range(Q):
    s,t = list(map(int, input().split()))
    tmp_tops = tops[:]
    if not used[s]:
        tmp_tops.append(s)
        used[s]=True
    if not used[t]:
        tmp_tops.append(t)
        used[t]=True
    tmp_edges = used_edges[:]
    for t1  in tmp_tops:
        if weight[t1][s]!=float("inf"):
            tmp_edges.append([weight[t1][s],t1,s])
        if weight[t1][t]!=float("inf"):
            tmp_edges.append([weight[t1][t],t1,t])
    u = UF(N)
    next_edgeds = []
    heapify(tmp_edges)
    ans = 0
    while len(tmp_edges) > 0:
        hc,hs,ht = heappop(tmp_edges)
        if u.same(hs,ht):continue
        u.unite(hs,ht)
        next_edgeds.append([hc,hs,ht])
        ans+=hc
    tops = tmp_tops
    used_edges = next_edgeds
    if not u.same(s,t):
        print("IMPOSSIBLE")
    else:
        print(ans)