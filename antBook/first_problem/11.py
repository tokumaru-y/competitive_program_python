N=int(input())
T=[int(input()) for _ in range(N)]
def GCD(x,y):
    if x<y:x,y=y,x
    if y==0:return x
    return GCD(y,x%y)
m = T[0]
ans = T[0]
for i in range(1,N):
    ans = (ans*T[i])//GCD(ans,T[i])
print(ans)