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
from heapq import heapify,heappop
H,W=list(map(int, input().split()))
[input() for _ in range(2)]
grid = [list(map(int, input().split())) for _ in range(H)]
ans = sum(map(sum, grid))
graph = []
for h in range(H):
    for w in range(W):
        if h>=1:graph.append([-(grid[h][w]*grid[h-1][w]), h*1000+w,(h-1)*1000+w])
        if w>=1:graph.append([-(grid[h][w]*grid[h][w-1]), h*1000+w,h*1000+(w-1)])
heapify(graph)
u = UF(1000**2+1)
while len(graph)>0:
    cost,x,y=heappop(graph)
    cost *=-1
    if u.same(x,y):continue
    u.unite(x,y)
    ans += cost
print(ans)