import math
N=int(input())
XY=[list(map(int, input().split())) for _ in range(N)]
dis = []
for x,y in XY:
    sx,sy = x-1,y
    ex,ey = x,y-1
    s = math.atan2(sy,sx)
    e = math.atan2(ey,ex)
    s = s + 2 * math.pi if s<0 else s
    e = e + 2 * math.pi if e<0 else e
    s = (s * 360) / (2*math.pi)
    e = (e * 360) / (2*math.pi)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    dis.append([s,e])
dis = sorted(dis, key= lambda x:(x[0],x[1]))
ans = 0
limit = float("-inf")
for e,s in dis:
    if limit <= s:
        ans += 1
        limit = e
print(ans)