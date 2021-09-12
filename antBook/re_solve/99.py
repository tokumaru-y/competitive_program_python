# https://atcoder.jp/contests/agc018/tasks/agc018_a
N,K=list(map(int, input().split()))
A=list(map(int, input().split()))
max_a = max(A)
if max_a < K:
    print("IMPOSSIBLE")
    exit()
def gcd(n,m):
    if n<m:n,m=m,n
    if m == 0:
        return n
    return gcd(m, n%m)
g = 0
for a in A:
    g = gcd(g,a)
if K%g != 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")