def gcd(n,m):
    if n<m:n,m=m,n
    if m == 0:
        return n
    return gcd(m, n%m)
def lcm(n,m):
    if n<m:n,m=m,n
    return (n*m) // gcd(n,m)