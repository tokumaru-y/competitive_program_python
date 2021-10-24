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
N,M=list(map(int, input().split()))
P=list(map(int, input().split()))
t = UF(N)
for _ in range(M):
    x,y = list(map(int, input().split()))
    x -= 1 
    y-=1
    t.unite(x,y)
ans = 0
for i in range(N):
    target = P[i]-1
    if t.same(target, i):ans+=1
print(ans)