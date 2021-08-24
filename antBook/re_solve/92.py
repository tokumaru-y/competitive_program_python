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
from heapq import heapify,heappop,heappush
N=int(input())
XY = []
for i in range(N):
    x,y = list(map(int, input().split()))
    XY.append([x,y,i])
sort_x = sorted(XY, key=lambda x: x[0])
sort_y = sorted(XY, key=lambda x: x[1])
graph = []
for i in range(N-1):
    graph.append([abs(sort_x[i+1][0] - sort_x[i][0]), sort_x[i+1][2],sort_x[i][2]])
    graph.append([abs(sort_y[i+1][1] - sort_y[i][1]), sort_y[i+1][2],sort_y[i][2]])
heapify(graph)
ans = 0
u=UF(N)
while len(graph) > 0:
    cost,s,t = heappop(graph)
    if u.same(s,t):continue
    ans+=cost
    u.unite(s,t)
print(ans)