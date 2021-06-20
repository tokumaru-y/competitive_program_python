a,b=list(map(int, input().split()))

def exGCD(a,b):
    if b>0:
        d, y, x = exGCD(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

d,x,y=exGCD(a,b)
print(x,y)