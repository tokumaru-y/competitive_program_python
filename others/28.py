A,B,C=list(map(int, input().split()))
def GCD(x,y):
    if x<y:x,y=y,x
    if y==0:return x
    return GCD(y,x%y)
g = GCD(A,B)
ans = "YES" if C%g==0 else "NO"
print(ans)