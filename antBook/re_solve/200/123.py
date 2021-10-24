# https://atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_d
N,M=list(map(int, input().split()))
X=[]
for _ in range(M):
    i = int(input())
    X.append(i-1)
def check(mid):
    checked_left = 0
    for i in range(M):
        dif = X[i]-checked_left
        if dif > mid:return False
        if dif <= 0:
            checked_left = max(X[i]+mid+1, checked_left)
        else:
            checked_left = max(X[i] - 2*dif + mid+1, X[i]+(mid-dif)//2 + 1)
            checked_left = min(checked_left, N)
    return checked_left >= N
right = 10**18
left = -1
while right - left > 1:
    mid = (right+left)//2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)