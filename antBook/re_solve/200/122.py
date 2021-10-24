# https://atcoder.jp/contests/abc026/tasks/abc026_d
from math import sin, pi
A,B,C=list(map(int, input().split()))
right = 10**5
left = 0
def calc(t):
    return A*t + B*sin(C*t*pi)
while abs(calc(right) - 100) > 10**-6:
    mid = (right+left) / 2
    time = calc(mid)
    if time > 100:
        right = mid
    else:
        left = mid
print(right)