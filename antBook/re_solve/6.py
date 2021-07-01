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

N,K,L=list(map(int, input().split()))
road_tree = UF(N)
train_tree = UF(N)
for _ in range(K):
    a,b = list(map(int, input().split()))
    a-=1
    b-=1
    road_tree.unite(a,b)
for _ in range(L):
    a,b = list(map(int, input().split()))
    a-=1
    b-=1
    train_tree.unite(a,b)
dict = {}
for i in range(N):
    rt = train_tree.root(i)
    rr = road_tree.root(i)
    if dict.get(rt) is None:
        dict[rt] = {}
    if dict[rt].get(rr) is None:
        dict[rt][rr] = 1
    else: 
        dict[rt][rr] += 1
ans = []
for i in range(N):
    rt = train_tree.par[i]
    rr = road_tree.par[i]
    ans.append(dict[rt][rr])
print(*ans)