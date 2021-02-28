class UnionFind():

    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.cnt = [1] * n
    
    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x]= self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px=self.find(x)
        py=self.find(y)
        if px == py:return
        if self.cnt[px] > self.cnt[py]:
            main, child = px,py
        else:
            main, child = py,px
        self.cnt[main] += self.cnt[child]
        self.par[child] = self.par[main]
    
    def get_cnt(self,x):
        return self.cnt[x]
    
    def is_union(self,x,y):
        if self.par[x] == self.par[y]:
            return False
        return True
N,M=list(map(int,input().split()))
uf = UnionFind(N)
for _ in range(M):
    a,b=list(map(int,input().split()))
    a,b=a-1,b-1
    if uf.is_union(a,b):uf.union(a,b)
ans = 0
for i in range(N):
    ans= max(ans, uf.get_cnt(i))
print(ans)