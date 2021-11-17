# https://atcoder.jp/contests/abc010/tasks/abc010_3
sx,sy,ex,ey,T,V = list(map(int, input().split()))
N=int(input())
XY=[list(map(int, input().split())) for _ in range(N)]
import math
for x,y in XY:
    a = math.sqrt((x-sx)**2 + (y-sy)**2)
    b = math.sqrt((x-ex)**2 + (y-ey)**2)
    if a + b <= T*V:
        print("YES")
        exit()
print("NO")