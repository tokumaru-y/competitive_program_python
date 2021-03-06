import math
N,D=list(map(int, input().split()))
ans=0
for _ in range(N):
    x,y=list(map(int,input().split()))
    distance = math.sqrt(x**2+y**2)
    if distance <= D:ans+=1
print(ans)