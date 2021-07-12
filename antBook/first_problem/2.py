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
XY=[]
for i in range(N):
    x,y=list(map(int, input().split()))
    XY.append([x,y,i])
X=sorted(XY,key=lambda x:x[0])
Y=sorted(XY,key=lambda x:x[1])
h = []
for i in range(1,N):
    a = X[i][0]-X[i-1][0]
    b = Y[i][1]-Y[i-1][1]
    h.append([a,X[i][2],X[i-1][2]])
    h.append([b,Y[i][2],Y[i-1][2]])
from heapq import heapify,heappush,heappop
ans = 0
cnt = 1
heapify(h)
while len(h) > 0:
    cost,t1,t2 = heappop(h)
    if U.same(t1,t2):
        continue
    U.unite(t1,t2)
    ans+=cost
print(ans)