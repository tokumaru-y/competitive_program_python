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

        else:
            self.par[ry] = rx
            self.deepth[rx] += self.deepth[ry]
    
    def same(self, x, y):
        return self.par[x] == self.par[y]
N,M=list(map(int, input().split()))
P=list(map(int,input().split()))
U = UnionFind(N)
ind_list = {}
for i,p in enumerate(P):
    ind_list[p]=i

for _ in range(M):
    a,b=list(map(lambda x : int(x)-1, input().split()))
    U.unite(a,b)
ans = 0
for i in range(N):
    ind = ind_list[i+1]
    if U.root(ind) == U.root(i):
        ans += 1
print(ans)
    