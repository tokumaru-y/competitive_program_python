from heapq import heapify,heappop,heappush
Q=int(input())
now_add = 0
hq=[]
for _ in range(Q):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        num = inp[1]
        num -= now_add
        heappush(hq,num)
    elif inp[0] == 2:
        num = inp[1]
        now_add += num
    else:
        target=heappop(hq)
        print(target+now_add)