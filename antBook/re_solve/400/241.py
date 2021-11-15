# https://atcoder.jp/contests/arc128/tasks/arc128_b
T=int(input())
def check(a,b,c):
    dif = abs(b-c)
    if dif%3==0:
        x = dif//3
        y = (b+c+x)//2
        return x+y
    else:
        return float("inf")
for _ in range(T):
    l = list(map(int, input().split()))
    a,b,c=l
    ans = float("inf")
    ans = min(ans,check(a,b,c))
    ans = min(ans,check(b,c,a))
    ans = min(ans,check(c,b,a))
    print(ans if ans < float("inf") else -1)