def gcd(n,m):
    if n<m:n,m=m,n
    if m == 0:
        return n
    return gcd(m, n%m)
def lcm(n,m):
    if n<m:n,m=m,n
    return (n*m) // gcd(n,m)
N=int(input())
ll = [int(input()) for _ in range(N)]
ans = ll[0]
for i in range(1,N):
    ans = lcm(ans,ll[i])
print(ans)