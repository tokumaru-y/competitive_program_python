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
sys.setrecursionlimit(10**6)
N=int(input())
A=[int(input())-1 for _ in range(N)]
U = UF(N)
type = [-1] * N
def dfs(x,t):
    type[x]=t
    nx=A[x]
    if type[nx] != -1:
        if type[x] == type[nx]:
            return False
        else:
            return True
    return dfs(nx, abs(t-1))
is_checked = [False]*N
for i in range(N):
    U.unite(i,A[i])
is_bin = True
for i in range(N):
    if is_checked[U.root(i)]:continue
    is_checked[U.root(i)]=True
    if not dfs(i,0):
        is_bin = False
if is_bin:
    b,w=0,0
    for t in type:
        if t==0:
            b+=1
        else:
            w+=1
    print(max(b,w))
else:
    print(-1)
    