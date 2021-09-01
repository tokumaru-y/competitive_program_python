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

N=int(input())
U=UF(N)
ans = 0
sort_list = []
for i in range(N-1):
    u,v,w = list(map(int, input().split()))
    u-=1
    v-=1
    sort_list.append([w,u,v])
sort_list = sorted(sort_list, key= lambda x:x[0])
for i in range(N-1):
    w,u,v = sort_list[i]
    ru, rv = U.root(u), U.root(v)
    du, dv = U.deepth[ru], U.deepth[rv]
    if du == 1 or dv == 1:
        ans += w*(max(du,dv))
    else:
        ans += w*(du*dv)
    U.unite(u,v)
print(ans)