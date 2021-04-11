import math
R,X,Y=list(map(int, input().split())) 
d = math.sqrt(X**2+Y**2)
if R == d:
    print(1)
elif d<=2*R:
    print(2)
else:
    print(math.ceil(d/R))