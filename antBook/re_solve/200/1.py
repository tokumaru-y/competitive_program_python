from heapq import heapify, heappush, heappop
N,K=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
ans = 0
h = []
for i in range(N):
    h.append([AB[i][0], AB[i][1]])
heapify(h)
while K > 0:
    time, plus_time = heappop(h)
    K-=1
    ans += time
    heappush(h, [time+plus_time, plus_time])
print(ans)