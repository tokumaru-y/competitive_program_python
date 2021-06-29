from heapq import heapify, heappop, heappush
N=int(input())
A=list(map(int, input().split()))
S = [0] * (N+1)
T = [0] * (N+1)
S[0] = sum(A[:N])
T[N] = sum(A[2*N:])
hs = A[:N]
ht = [ -1*a for a in A[2*N:]]
heapify(hs)
heapify(ht)

for i in range(N, 2*N):
    s = hs[0]
    if s < A[i]:
        S[i+1-N] = S[i-N] + A[i] + s
        heappop(hs)
        heappush(hs, A[i])
    else:
        S[i+1-N] = S[i-N]

for i in reversed(range(N, 2*N)):
    t = -ht[0]
    if t > A[i]:
        T[i-N-1] = T[i-N] + t - A[i]
        heappop(ht)
        heappush(ht, -A[i])
    else:
        T[i-N-1] = T[i-N]
ans = float("-inf")
for i in range(N+1):
    ans = max(ans, S[i] - T[i])
print(ans)
