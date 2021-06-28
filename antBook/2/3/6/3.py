from bisect import bisect_left
N=int(input())
box=[list(map(int, input().split())) for _ in range(N)]
box_A = sorted(box, key = lambda x : (x[0], x[1]))
box_B = sorted(box, key = lambda x : (x[1], x[0]))
dp=[float('inf')] * N
used_w = {}
used_h = {}
for h,w in box_A:
    if used_h.get(h, False):
        continue
    used_h[h]=True
    i=bisect_left(dp, w)
    dp[i] = w
ans = 0
for i in reversed(range(N)):
    if dp[i] < float("inf"):
        ans = i+1
        break
dp=[float('inf')] * N
for h,w in box_B:
    if used_w.get(w, False):
        continue
    used_w[w] = True
    i=bisect_left(dp, h)
    dp[i] = h

for i in reversed(range(N)):
    if dp[i] < float("inf"):
        ans = max(ans, i+1)
        break
print(ans)
