N=int(input())
AB=[list(map(int, input().split())) for _ in range(N)]
sum_a = 0
for a,b in AB:
    sum_a += a

right = sum_a
left = 0
while abs(right-left) > 10**(-5):
    # 地点
    mid = (right+left) / 2
    left_time = 0
    right_time = 0
    tmp_mid = mid
    tmp_dis = 0
    # そこに行くまでの時間を以て、同じかを判断する
    for a, b in AB:
        if tmp_mid <= 0:break
        need_time = a / b
        if tmp_dis + a >= tmp_mid:
            left_time += (tmp_mid-tmp_dis) / b
            tmp_mid = 0
            break
        else:
            left_time += need_time
            tmp_dis += a

    tmp_mid = sum_a - mid
    tmp_dis = 0
    # そこに行くまでの時間を以て、同じかを判断する
    for i in reversed(range(N)):
        if tmp_mid <= 0:break
        a,b = AB[i]
        need_time = a / b
        if tmp_dis + a >= tmp_mid:
            right_time += (tmp_mid-tmp_dis) / b
            tmp_mid = 0
            break
        else:
            right_time += need_time
            tmp_dis += a
    if left_time >= right_time:
        right = mid
    else:
        left = mid

print(left)
    
