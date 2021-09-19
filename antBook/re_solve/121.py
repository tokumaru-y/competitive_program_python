# https://atcoder.jp/contests/arc050/tasks/arc050_b
R,B=list(map(int, input().split()))
X,Y=list(map(int, input().split()))
def check(mid):
    if R-mid < 0 or B-mid < 0:return False
    m = (R-mid)//(X-1)
    n = (B-mid)//(Y-1)
    return (m+n) >= mid
right = 10**20
left = 0
while right - left > 1:
    mid = (right+left)//2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)