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



H,W=list(map(int, input().split()))
sx,sy=list(map(int, input().split()))
ex,ey=list(map(int, input().split()))
sx-=1
sy-=1
ex-=1
ey-=1
grid = [list(map(int, input().split())) for _ in range(H)]
uf = UnionFind(H*W)
nodes = []
hi=[1,0,-1,0]
wi=[0,1,0,-1]
ans = 0
for h in range(H):
    for w in range(W):
        ans += grid[h][w]
        for i in range(4):
            nh, nw = h+hi[i], w+wi[i]
            if not(0<=nh<H and 0<=nw<W):continue
            nodes.append([grid[h][w]*grid[nh][nw], h+w, nh+nw])
print(ans)
nodes.sort(reverse=True)
for n in nodes:
    point, h, w = n
    if not uf.same(h,w):
        ans += point
        uf.unite(h,w)
print(ans)