from heapq import heapify, heappop, heappush
N=int(input())
A=list(map(int, input().split()))
S = [0] * (N*2+1)
T = [0] * (N*2+1)
s = []
t = []
for i in range(N):
    S[i+1] = S[i] + A[i]
    s.append(A[i])
for index, i in enumerate(reversed(range(N*2,N*3))):
    T[index+1] = T[index] + A[i]
    t.append(-A[i])
heapify(s)
heapify(t)
for i in range(N, N*2):
    top = s[0]
    if top < A[i]:
        S[i+1] = S[i] + A[i] - top
        heappop(s)
        heappush(s, A[i])
    else:
        S[i+1] = S[i]
for index, i in enumerate(reversed(range(N, N*2))):
    top = -t[0]
    if top > A[i]:
        T[index+N+1] = T[index+N] + A[i] - top
        heappop(t)
        heappush(t, -A[i])
    else:
        T[index+N+1] = T[index+N]
ans = float("-inf")
for i in range(N,N*2+1):
    ans = max(ans, S[i] - T[N*3-i])
print(ans)