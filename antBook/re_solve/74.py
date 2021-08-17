from heapq import heapify,heappush,heappop
N=int(input())
A=list(map(int, input().split()))
pre_h = []
back_h = []
ans = 0
for i in range(N):
    pre_h.append(A[i])
    back_h.append(-A[-(i+1)])
    ans += A[i] - A[-(i+1)]
heapify(pre_h)
heapify(back_h)
tmp_ans = ans

for i in range(N,2*N):
    next_num = A[i]
    next_pre = heappop(pre_h)
    next_back = heappop(back_h)
    dif_pre = next_num - next_pre
    dif_back = -next_back - next_num
    if dif_pre >= dif_back:
        heappush(pre_h, next_num)
        heappush(back_h, next_back)
        tmp_ans = tmp_ans - next_pre + next_num
    else:
        heappush(back_h, -next_num)
        heappush(pre_h, next_pre)
        tmp_ans = tmp_ans - next_back - next_num
    ans = max(ans, tmp_ans)
    print(pre_h)
    print(back_h)
    print(ans,tmp_ans)
print(ans)