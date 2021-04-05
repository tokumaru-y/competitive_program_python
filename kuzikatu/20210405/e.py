N=int(input())
A=list(map(int, input().split()))
plus = []
minus = []
for a in A:
    if a >= 0:
        plus.append(a)
    else:
        minus.append(a)
plus.sort()
minus.sort()
if len(minus) == 0:
    tmp_sum = 0
    for i in range(1,len(plus)-1):
        tmp_sum += plus[i-1] - plus[i]
    ans = plus[-1] - tmp_sum
elif len(plus) == 0:
    tmp_sum = 0
    for i in reversed(range(1,len(minus)-1)):
        tmp_sum += minus[i] - minus[i-1]
    ans = tmp_sum - minus[0]
else:
    tmp_sum = 0
    sum_list = minus[1:] + plus[:len(plus)]
    for i in range(1,len(sum_list)):
        tmp_sum += sum_list[i] - sum_list[i-1]
    ans = (plus[-1] - minus[0]) - tmp_sum
print(ans)