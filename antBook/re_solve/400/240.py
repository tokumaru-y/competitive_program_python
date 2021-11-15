# https://atcoder.jp/contests/agc036/tasks/agc036_a
S=int(input())
import math
a = math.isqrt(S)+1
if a > 10**9:a-=1
b = a
c = S - (a*b) if S >= (a*b) else a*b - S
d = 1
print(a,d,c,b,0,0)
