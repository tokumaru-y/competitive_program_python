# https://atcoder.jp/contests/abc104/tasks/abc104_c
import math
D,G=list(map(int, input().split()))
PC = [list(map(int, input().split())) for _ in range(D)]
ans = float("inf")
for bit in range(1<<D):
    tmp = 0
    last_idx = 0
    solve_cnt = 0
    for i in range(D):
        if bit & (1<<i):
            tmp += 100*(i+1) * PC[i][0] + PC[i][1]
            solve_cnt += PC[i][0]
        else:
            last_idx = i
    if tmp < G:
        left = G - tmp
        need = math.ceil(left / (100*(last_idx+1)))
        if need >= PC[last_idx][0]:continue
        solve_cnt += need
    ans = min(ans, solve_cnt)
print(ans)