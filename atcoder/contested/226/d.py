import math
def reduce(p, q):
    common = math.gcd(p, q)
    return (p // common, q // common)
N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
lis = []
for i in range(N):
    f = XY[i]
    for j in range(i+1,N):
        g = XY[j]
        x = f[0] - g[0]
        y = f[1] - g[1]
        x,y = reduce(x,y)
        lis.append((-x,-y))
        lis.append((x,y))
s = list(set(lis))
print(len(s))