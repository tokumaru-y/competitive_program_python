# TODO 解けない
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2706
P,Q=list(map(int, input().split()))
def GCD(x,y):
    if x<y:x,y=y,x
    if y==0:
        return x
    return GCD(y,x%y)
g = GCD(P,Q)
print(Q//g)