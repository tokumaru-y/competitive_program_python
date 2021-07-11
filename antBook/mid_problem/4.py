N=int(input())
ballons = [list(map(int, input().split())) for _ in range(N)]
left = 0
right = 10**15
def check(value):
    check_value = float("inf")
    for h,s in ballons:
        tmp=h+(N-1)*s
        check_value=min(tmp,check_value)
    if check_value>value:
        return False
    else:
        return True

while right - left > 1:
    mid = (left+right)//2
    is_correct = check(mid)
    if is_correct:
        right=mid
    else:
        left=mid
print(right)