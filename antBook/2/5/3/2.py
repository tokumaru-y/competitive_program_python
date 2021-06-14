from heapq import heapify, heappop, heappush
class UnionFind:
    
    def __init__(self,x):
        self.par = [i for i in range(x)]
        self.deepth = [1 for _ in range(x)]
    
    def root(self,x):
        if x == self.par[x]:return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def same(self,x,y):
        return self.root(x) == self.root(y)
    
    def unite(self, x,y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry :return True
        if self.deepth[rx] < self.deepth[ry]:
            rx,ry = ry, rx
        self.par[ry] = rx
        self.deepth[rx] += self.deepth[ry]

N=int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
edges = []
sort_a = []
sort_b = []
for i in range(N):
    sort_a.append([XY[i][0], i])
    sort_b.append([XY[i][1], i])
ans = 0
sort_a.sort()
sort_b.sort()
for i in range(N-1):
    edges.append([sort_a[i+1][0] - sort_a[i][0], sort_a[i+1][1], sort_a[i][1]])
    edges.append([sort_b[i+1][0] - sort_b[i][0], sort_b[i+1][1], sort_b[i][1]])

uf = UnionFind(N)
heapify(edges)
while len(edges) > 0:
    dis, a, b = heappop(edges)
    if not uf.same(a,b):
        uf.unite(a,b)
        ans += dis
print(ans)
