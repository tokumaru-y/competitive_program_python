N,X=list(map(int, input().split()))
L=list(map(int, input().split()))
L.append(X)
distances=[]
L.sort()
for i in range(1,len(L)):
    distances.append(L[i] - L[i-1])
distances.sort()
def GCD(x,y):
    if x<y:x,y=y,x
    if y==0:return x
    return GCD(y,x%y)
res=0
for d in distances:
    res=GCD(res,d)
print(res)