A,B=list(map(int, input().split()))
def GCD(x,y):
    if x<y:x,y=y,x
    if y==0:return x
    return GCD(y,x%y)
g = GCD(A,B)
a,b=A//g,B//g
ans = g*GCD(a+b,g)
print(ans)