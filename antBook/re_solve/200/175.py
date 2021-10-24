# https://atcoder.jp/contests/arc004/tasks/arc004_1
import math
N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    x,y=XY[i]
    for j in range(i+1,N):
        a,b=XY[j]
        ans = max(ans, math.sqrt((x-a)**2 + (y-b)**2))
print(ans)