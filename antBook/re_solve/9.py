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


N,Q=list(map(int, input().split()))
U=UF(2*N)
for _ in range(Q):
    w,x,y,z=list(map(int, input().split()))
    x-=1
    y-=1
    if w == 1:
        if z%2 == 0:
            U.unite(2*x, 2*y)
            U.unite(2*x+1, 2*y+1)
        else:
            U.unite(2*x, 2*y+1)
            U.unite(2*x+1, 2*y)
    else:
        print("YES" if U.same(x*2, y*2) else "NO")
