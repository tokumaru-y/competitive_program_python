from heapq import heapify, heappop, heappush
N=int(input())
A=list(map(int, input().split()))
half_a = A[:N]
half_b = sorted([-1*a for a in A[N:]])[:N]
heapify(half_a)
heapify(half_b)
ans = sum(A[:N]) - sum(sorted([-1*a for a in A[N:]])[:N])
for i in range(N,2*N):
    a = A[i]
    ha=heappop(half_a)
    hb=heappop(half_b)
    dif_a = a - ha
    dif_b = -a - hb