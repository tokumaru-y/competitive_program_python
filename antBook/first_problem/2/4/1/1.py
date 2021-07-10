from heapq import heapify, heappop, heappush
N,K=list(map(int, input().split())) 
d = []
for _ in range(N):
    a,b = list(map(int ,input().split()))
    d.append([a,b])
heapify(d)
ans = 0
for _ in range(K):
    a,b = heappop(d)
    heappush(d, [a+b,b])
    ans += a
print(ans)
