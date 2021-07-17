N,X=list(map(int, input().split()))
def GCD(x,y):
    if x>y:x,y=y,x
    if y == 0: return x
    if y % x == 0:
        return ((y//x)*2-1) * x
    else:
        return (y//x)*2*x + GCD(y%x, x)
ans = N + GCD(X,N-X)
print(ans)