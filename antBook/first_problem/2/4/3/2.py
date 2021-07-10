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
    
N,K,L = list(map(int, input().split()))
A = UnionFind(N)
B = UnionFind(N)
for _ in range(K):
    a,b=list(map(lambda x : int(x)-1, input().split()))
    A.unite(a,b)
for _ in range(L):
    a,b=list(map(lambda x : int(x)-1, input().split()))
    B.unite(a,b)
counter = {}
for i in range(N):
    ra = A.root(i)
    rb = B.root(i)
    target = (ra,rb)
    if target in counter:
        counter[target]+=1
    else:
        counter[target]=1
ans = []
for i in range(N):
    ra = A.root(i)
    rb = B.root(i)
    target = (ra,rb)
    ans.append(counter[target])
print(*ans)