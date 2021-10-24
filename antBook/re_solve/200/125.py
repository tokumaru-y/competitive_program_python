# https://atcoder.jp/contests/abc034/tasks/abc034_d
N,K=list(map(int, input().split()))
WP=[list(map(int, input().split())) for _ in range(N)]
def check(mid):
    tmp_list = []
    for idx ,wp in enumerate(WP):
        w,p = wp
        dif = (p-mid)*w
        tmp_list.append([dif, idx])
    tmp_list.sort(reverse=True)
    total = sum([x for x,_ in tmp_list[:K]])
    return total >= 0
right = 10**10
left = 0
for _ in range(1000):
    mid = (right+left)/2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)