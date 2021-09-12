# https://atcoder.jp/contests/arc026/tasks/arc026_4
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
    
N,M=list(map(int, input().split()))
ABCT=[list(map(int, input().split())) for _ in range(M)]
def check(value):
    U=UF(N)
    ll = []
    for a,b,c,t in ABCT:
        a-=1
        b-=1
        cost = c-value*t
        ll.append([cost,a,b])
    ll.sort()
    total_cost = 0
    for i in range(len(ll)):
        cost, x, y = ll[i]
        if cost < 0 or not U.same(x,y):
            total_cost += cost
            U.unite(x,y)
    if total_cost <= 0:
        return True
    else:
        return False

left = 0
right = 10**9
for _ in range(100):
    mid = (right + left) / 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)