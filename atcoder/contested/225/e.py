from math import inf
N=int(input())
XY=[list(map(int, input().split())) for _ in range(N)]
dis = []
for x,y in XY:
    sx,sy = x-1,y
    ex,ey = x,y-1
    s = (10 ** 20 * (sy)//(sx)) if sx != 0 else inf
    e = (10 ** 20 * (ey)//(ex)) if ey != 0 else -1
    dis.append([s,e])
dis = sorted(dis, key= lambda x:(x[0],x[1]))
ans = 0
limit = float("-inf")
for e,s in dis:
    if limit <= s:
        ans += 1
        limit = e
print(ans)