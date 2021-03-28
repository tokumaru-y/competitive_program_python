from math import pi, sqrt, sin, cos, radians, degrees
N=int(input())
x0,y0=list(map(int,input().split()))
x,y = list(map(int, input().split()))
r = 2*pi/N
cx,cy = (x0+x)/2, (y0+y)/2
x0, y0 = x0-cx, y0-cy
ansx, ansy = [x0*cos((r))-y0*sin((r))+ cx, x0*sin((r))+y0*cos((r)) + cy]
print(ansx, ansy)