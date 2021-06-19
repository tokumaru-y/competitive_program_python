N=int(input())
l=[int(input()) for _ in range(N)]
def GCD(x,y):
    if x<y:x,y=y,x
    if y == 0:return x
    return GCD(y, x%y)
def LCD(x,y):
    g = GCD(x,y)
    return x*y//g
g=l[0]
for i in range(1,N):
    g=LCD(g,l[i])
print(g)