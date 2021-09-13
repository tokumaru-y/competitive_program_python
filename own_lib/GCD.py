def gcd(n,m):
    if n<m:n,m=m,n
    if m == 0:
        return n
    return gcd(m, n%m)
def lcm(n,m):
    if n<m:n,m=m,n
    return (n*m) // gcd(n,m)

def ext_gcd(a, b):
    if b:
        d, y, x = ext_gcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0