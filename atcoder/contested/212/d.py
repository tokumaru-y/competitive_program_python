Q=int(input())
from heapq import heapify,heappop,heappush
h = []
heapify(h)
total_sum = [0] * (Q+1)
print_ind = []
for i in range(Q):
    tmp = list(map(int, input().split()))
    total_sum[i+1] = total_sum[i]
    if tmp[0] == 1:
        x = tmp[1]
        heappush(h, x - total_sum[i+1])
    elif tmp[0] == 2:
        total_sum[i+1] += tmp[1]
    else:
        target = heappop(h)
        print(target+total_sum[i+1])
