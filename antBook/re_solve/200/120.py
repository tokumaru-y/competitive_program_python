# https://atcoder.jp/contests/abc023/tasks/abc023_d
N=int(input())
HS=[list(map(int, input().split())) for _ in range(N)]
def check(mid):
    tmp_list = []
    for h,s in HS:
        if h>mid:return False
        tmp_list.append((mid-h)//s)
    tmp_list.sort()
    for idx, t in enumerate(tmp_list):
        if idx>t:return False
    return True

right = 10**20
left = 0
while right-left > 1:
    mid = (right+left)//2
    if check(mid):
        right=mid
    else:
        left=mid
print(right)