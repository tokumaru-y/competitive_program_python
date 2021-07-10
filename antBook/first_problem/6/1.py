import math
N=int(input())
XY=[list(map(int, input().split())) for _ in range(N)]
ans = float('-inf')
for i in range(N):
    for j in range(i+1, N):
        x,y = XY[i]
        a,b = XY[j]
        d = math.sqrt((x-a)**2 + (y-b)**2)
        ans = max(ans, d)
print(ans)