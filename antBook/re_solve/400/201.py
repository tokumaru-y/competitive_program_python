# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b
N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]
arms = []
for x,l in XL:
    left = x-l
    right = x+l
    arms.append([right, left])
arms.sort()
ans = 0
_right = float("-inf")
for right, left in arms:
    if _right <= left:
        ans += 1
        _right = right
print(ans)