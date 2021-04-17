class UnionFind:
    def __init__(self, x):
        self.par = [i for i in range(x)]
        self.deepth = [1 for _ in range(x)]
        # 親からの距離
        self.distance = [0 for _ in range(x)]

    def root(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def unite(self, x, y, z):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return
        if self.deepth[rx] < self.deepth[ry]:
            self.par[rx] = ry
            self.deepth[ry]+=self.deepth[rx]
        else:
            self.par[ry] = rx
            self.deepth[rx] += self.deepth[ry]
    
    def same(self, x, y):
        return self.par[x] == self.par[y]
N,Q=list(map(int, input().split()))
U = UnionFind(N)
for _ in range(Q):
    w,x,y,z = list(map(int, input().split()))
