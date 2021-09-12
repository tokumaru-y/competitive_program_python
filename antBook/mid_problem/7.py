# https://atcoder.jp/contests/abc034/tasks/abc034_d
N,K=list(map(int, input().split()))
WP=[list(map(int, input().split())) for _ in range(N)]
def check(value):
    waters = []
    for idx, wp in enumerate(WP):
        dif = ((value-wp[1]) / 100)*wp[0]
        waters.append([dif,idx])
    waters.sort()
    total_water = 0
    total_salt = 0
    for dif, idx in waters[:K]:
        water,p = WP[idx]
        total_water += water
        total_salt += water * (p / 100)
    if (total_salt / total_water ) * 100 >= value:
        return True
    else:
        return False

right = 0
left = 10**9
for _ in range(100):
    mid = (right + left) / 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)