from heapq import heapify,heappop,heappush
N,K=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
h=[]
for a,b in AB:
    h.append([a, b])
heapify(h)
ans = 0
for _ in range(K):
    need_times, add_time = heappop(h)
    ans += need_times
    heappush(h, [need_times+add_time, add_time])
print(ans)