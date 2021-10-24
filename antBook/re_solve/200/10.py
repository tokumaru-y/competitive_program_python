class WUF:
    """重みつきUnion Find
    UF(x):
    self.par:　各頂点の親を表す
    self.deepth: 頂点の深さ表す
    self.weight: 親までの距離を表す
    """
    def __init__(self, x):
        """[summary]

        Args:
            x (int): 頂点数
        """
        self.par = [i for i in range(x)]
        self.deepth = [1 for _ in range(x)]
        self.weight = [0 for _ in range(x)]
    
    def root(self, x):
        """[summary]
            頂点の親を探索する。ついでに親頂点の探索回数も減らす
        Args:
            x ([int]): 探索対象の頂点

        Returns:
            int: 頂点の親頂点
        """
        if x == self.par[x]: return x
        res = self.root(self.par[x])
        self.weight[x] += self.weight[self.par[x]]
        self.par[x] = res
        return self.par[x]
    
    def same(self, x, y):
        """[summary]
            2頂点が同じグループに属するか
        Args:
            x ([int]): 頂点
            y ([int]): 頂点

        Returns:
            boolean: x,yが同じグループに属しているか
        """
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry
    
    def unite(self, x, y, w):
        """[summary]
            2頂点を結び、頂点間の距離も記憶する
        Args:
            x ([int]): 頂点
            y ([int]): 頂点
            w ([int]): 辺の重み
        Returns:
            boolean:
            　True: 各頂点が違う親で結びつけられた
            　False: 各頂点が同じ親だった
        """
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:return False
        if self.deepth[rx] < self.deepth[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.deepth[rx] == self.deepth[ry]:
                self.deepth[rx] += 1
        return True
    
    def diff(self, x, y):
        """[summary]
            2頂点間の距離を返す
        Args:
            x ([int]): 頂点
            y ([int]): 頂点
        Returns:
            int: xからyの距離
        """
        return self.weight[x] - self.weight[y]

N,M=list(map(int, input().split()))
U=WUF(N)
for _ in range(M):
    l,r,d = list(map(int, input().split()))
    l-=1
    r-=1
    if U.same(l,r):
        if U.diff(l,r) != d:
            print("No")
            exit()
    else:
        U.unite(l,r,d)
print("Yes")