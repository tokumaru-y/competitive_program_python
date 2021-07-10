class UnionFind:
    def __init__(self, x):
        self.par = [i for i in range(x)]
        self.deepth = [1 for _ in range(x)]
    
    def root(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return
        if self.deepth[rx] < self.deepth[ry]:
            self.par[rx] = ry
            self.deepth[ry]+=self.deepth[rx]
            self.deepth[rx] = 0
        else:
            self.par[ry] = rx
            self.deepth[rx] += self.deepth[ry]
            self.deepth[ry] = 0
    
    def same(self, x, y):
        return ("Yes" if self.par[x] == self.par[y] else "No")


N,Q=list(map(int, input().split()))
uf = UnionFind(N)
for _ in range(Q):
    p,a,b=list(map(int, input().split()))
    if p == 0:
        uf.unite(a,b)
    else:
        print(uf.same(a,b))