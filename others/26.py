N=int(input())
X=list(map(int, input().split()))
def GCD(x,y):
    if x<y:x,y=y,x
    if y==0:return x
    return GCD(y,x%y)
ans = 0
for x in X:
    ans = GCD(ans, x)
print(ans)