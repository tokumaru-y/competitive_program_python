N=int(input())
ballons = [list(map(int, input().split())) for _ in range(N)]
left = 0
right = 10**15
def check(value):
    check_value = float("inf")
    times = []
    for h,s in ballons:
        if h>value:return False
        t = (value-h)/s
        times.append(t)
    times.sort()
    for i in range(N):
        if times[i] < i:
            return False
    return True
while right - left > 1:
    mid = (left+right)//2
    is_correct = check(mid)
    if is_correct:
        right=mid
    else:
        left=mid
print(right)