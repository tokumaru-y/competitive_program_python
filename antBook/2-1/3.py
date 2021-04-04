D,G=list(map(int, input().split()))
pc=[list(map(int, input().split())) for _ in range(D)]
ans = float('inf')
for bit in range(1<<D):
    point = 0
    cnt = 0
    left_max = 0
    for i in range(D):
        if bit & 1<<i:
            p,c = pc[i]
            point += 100*(i+1)*p+c
            cnt += p
        else:
            if 100*(i+1)*pc[i][0] > left_max:
                left_max = i
    if point >= G:
        ans = min(ans, cnt)
    else:
        left_point = G-point
        lp,lc = pc[left_max]
        if 100*(left_max+1)*(lp-1) >= left_point:
            add_cnt = left_point//(100*(left_max+1)) if left_point%(100*(left_max+1)) == 0 else left_point//(100*(left_max+1)) + 1
            ans = min(ans, add_cnt+cnt)
print(ans)