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
import sys
sys.setrecursionlimit(10**9)
N=int(input())
A=[int(input()) for _ in range(N)]
U = UF(N)
colors = [-1]*N
for i in range(N):
    x,y = max(i,A[i]-1), min(i,A[i]-1)
    U.unite(x,y)
is_ok = True
def dfs(t,c):
    res = True
    nt = A[t]-1
    if colors[nt] == c:
        return False
    elif colors[nt] > -1:
        return True
    colors[nt] = abs(c-1)
    res = dfs(nt, abs(c-1))
    return res
ans = 0
for i in range(N):
    if colors[i] > -1:continue
    colors[i]=0
    if not dfs(i,0):
        print(-1)
        exit()
    ans += U.deepth[i]//2 if U.deepth[i]%2==0 else U.deepth[i]//2 + 1
print(ans)