class UnionFind:

    def __init__(self, x):
        self.par = [a for a in range(x)]
        self.deepth = [1 for _ in range(x)]

    def root(self, x):
        if x == self.par[x]:return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry : return True
        if self.deepth[rx] > self.deepth[ry]:
            rx, ry = ry, rx
        self.par[rx] = ry
        self.deepth[ry] += self.deepth[rx]
    
    def same(self, x, y):
        return self.root(x) == self.root(y)


from heapq import heapify, heappop
H,W=list(map(int, input().split()))
sx,sy=list(map(int, input().split()))
ex,ey=list(map(int, input().split()))
sx-=1
sy-=1
ex-=1
ey-=1
grid = [list(map(int, input().split())) for _ in range(H)]
uf = UnionFind(10**6)
nodes = []
ans = 0
for h in range(H):
    for w in range(W):
        ans += grid[h][w]
        if 0<h:nodes.append([-1*grid[h-1][w]*grid[h][w], (h-1)*1000**3 + w*1000**2 + h*1000+w])
        if 0<w:nodes.append([-1*grid[h][w-1]*grid[h][w], h*1000**3 + (w-1)*1000**2 + h*1000+w])
heapify(nodes)
while len(nodes) > 0:
    point, n = heappop(nodes)
    h = n // 10**6
    w = n % 10**6
    if not uf.same(h,w):
        ans += -1*point
        uf.unite(h,w)
print(ans)