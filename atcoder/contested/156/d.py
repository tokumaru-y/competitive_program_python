N,a,b = list(map(int,input().split()))
ans = 1
MOD = 10**9+7
def calc(x,num):
    global ans
    if x%2 == 1:
        x -=1
        c = calc(x, num)
        ans *= c
    elif x>0:
        x//=2
        c = calc(x, num)
        ans *= (c*c)%MOD
    ans%=MOD