# N,K=list(map(int,input().split()))
# H=list(map(int,input().split()))

# class UF():
#     def __init__(self, x):
#         self.par =  [i for i in range(x)]
#         self.high = [0 for i in range(x)]
#     def root(self,x):
#         if self.par[x]==x:return x
#         self.par[x] = self.root(self.par[x])
#         return self.par[x]
    
#     def unite(self, x, y):
#         rx = self.root(self.par[x])
#         ry = self.root(self.par[y])
#         if rx == ry :return True
#         if self.high[rx] >= self.high[ry]:
#             self.par[ry] = rx
#             self.high[ry] = self.high[rx]
#         else:
#             self.par[rx] = ry
#             self.par[ry] = self.high[rx]

# uf = UF(N)
# for i in range(N):
#     uf.high[i] = H[i]
# for _ in range(K):
#     a,b =list(map(int,input().split()))
#     a,b=a-1,b-1
#     uf.unite(a,b)
# par_set = set(uf.par)
# high_set = []
# print(len(set(uf.par)))
N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
max_high = [-1] * N
for i in range(K):
    a,b=list(map(lambda x : int(x) - 1, input().split()))
    max_high[a]= max(max_high[a], A[b])
    max_high[b]= max(max_high[b], A[a])
ans = 0
for i in range(N):
    if A[i] > max_high[i]:ans+=1
print(ans)