N,M,X=list(map(int,input().split()))
ans = float('inf')
money = [list(map(int,input().split())) for _ in range(N)]

for b in range(1<<N):
    tmp_sum = [0] * M
    tmp_m = 0
    for i in range(N):
        if b & 1<<i:
            tmp_m += money[i][0]
            for index, m in enumerate(money[i][1:]):
                tmp_sum[index-1]+=m
    if min(tmp_sum) >= X:
        ans = min(ans, tmp_m)
print(ans if ans!=float('inf') else -1)