# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=ja
def ext_gcd(a, b):
    if b:
        d, y, x = ext_gcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
A,B=list(map(int, input().split()))
_,x,y = ext_gcd(A,B)
print(x,y)