import sys
sys.setrecursionlimit(10**9)
class UnionFind:

    def __init__(self, x):
        self.par = [i for i in range(x)]
        self.ele = [1 for _ in range(x)]
    
    def root(self, x):
        if x == self.par[x]:return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:return True
        if self.ele[rx]<self.ele[ry]:
            self.ele[ry]+=self.ele[rx]
            self.par[rx] = ry
        else:
            self.ele[rx]+=self.ele[ry]
            self.par[ry] = rx
    def count(self, x):
        return self.ele[self.root(x)]

N=int(input())
members = [int(input())-1 for _ in range(N)]

uf = UnionFind(N)
for ind, mem in enumerate(members):
    uf.unite(ind, mem)
ans = 0
checked = [False]*N
for i in range(N):
    if checked[uf.root(i)]:continue
    checked[uf.root(i)] = True
    if uf.count(i)%2==1:
        print(-1)
        exit()
    ans += uf.count(i)//2
print(ans)