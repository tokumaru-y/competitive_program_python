class UF:
    def __init__(self, x):
        self.par = [i for i in range(x)]
        self.deepth = [1 for _ in range(x)]
    
    def root(self, x):
        if x == self.par[x]: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry
    
    def unite(self, x, y):
        """もし、すでに同じグループならFalseを返す.
        """
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:return False
        if self.deepth[rx] > self.deepth[ry]: rx, ry = ry, rx
        self.deepth[ry] += self.deepth[rx]
        self.par[rx] = self.par[ry]
N,Q = list(map(int, input().split()))
uf = UF(N)
for _ in range(Q):
    p,a,b = list(map(int, input().split()))
    if p == 0:
        uf.unite(a,b)
    elif p == 1:
        print("Yes" if uf.same(a,b) else "No")