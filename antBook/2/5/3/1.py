from heapq import heapify, heappush, heappop
class UnionFind:
    def __init__(self,x):
        self.par = [a for a in range(x)]
        self.deepth = [1 for _ in range(x)]
    
    def root(self, x):
        if x == self.par[x]:return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def unite(self,x,y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:return True
        if self.deepth[rx]<self.deepth[rx]:
            rx,ry = ry,rx
        self.par[rx] = ry
        self.deepth[ry]+=self.deepth[rx]
    
    def same(self, x,y):
        return self.root(x) == self.root(y)
    
V,E = list(map(int, input().split()))
ans = 0
graph = []
for _ in range(E):
    s,t,w=list(map(int, input().split()))
    graph.append([w,(s,t)])
uf = UnionFind(V)
graph.sort()
for i in range(E):
    w,st = graph[i]
    s,t = st
    if not uf.same(s,t):
        ans += w
        uf.unite(s,t)
print(ans)