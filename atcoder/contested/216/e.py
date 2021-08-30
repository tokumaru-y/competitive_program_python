from heapq import heapify, heappop,heappush
N,K=list(map(int, input().split()))
A=list(map(int,input().split()))
A.sort(reverse=True)
ans = 0
tmp_cnt = 0
for i in range(N):
    if i < N-1:
        dif = A[i] - A[i+1]
        
    else:
        if K>=A[i]:
            #TASUDAKE