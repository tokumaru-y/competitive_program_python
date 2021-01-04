from sys import stdin
import math

def solve(a,b,c,x,y):
    res = float('inf')
    # a,bのみ
    res = a * x + b * y
    # ab使用
    focas_a = c * x * 2 + b * (max(0,y-x))
    res = min(res,focas_a)
    focas_b = c * y * 2 + a * (max(0,x-y))
    res = min(res,focas_b)
    return res

if __name__ == "__main__":
    a,b,c,x,y = [int(x) for x in stdin.readline().rstrip().split()]
    ans = solve(a,b,c,x,y)
    print(ans)