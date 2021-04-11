import math
R,X,Y=list(map(int, input().split())) 
d = math.sqrt(X**2+Y**2)
d2 = math.isqrt(X**2+Y**2)
f = d2
if math.ceil(d) > d2:
    f = math.ceil(d)
ans = (f//R)
if not f%R==0: ans += 1
print(int(ans))