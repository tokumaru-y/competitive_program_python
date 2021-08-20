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
N,K,L=list(map(int, input().split()))
roads = UF(N)
rails = UF(N)
for _ in range(K):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    roads.unite(a,b)
for _ in range(L):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    rails.unite(a,b)
count_list = {}
for i in range(N):
    rx = roads.root(i)
    ry = rails.root(i)
    if (rx,ry) in count_list:
        count_list[(rx,ry)] += 1
    else:
        count_list[(rx,ry)] = 1
ans = []
for i in range(N):
    rx,ry = roads.root(i), rails.root(i)
    ans.append(count_list[(rx,ry)])
print(*ans)