N=int(input())
height=[0]*N
num = [float('inf')]*N
for _ in range(N):
    a=int(input())
    for i in range(N):
        if num[i] >= a:
            height[i] += 1
            num[i] = a
            break
ans = 0
for h in height:
    if h>0:ans+=1
print(ans)