# https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho3
N=int(input())
A=[int(input()) for _ in range(N)]
total = 0
accumulations = [0] * (N*2)
for i in range(N):
    total+=A[i]
    accumulations[i] = A[i]
    accumulations[i+N] = A[i]
left = 0
right = 10**18
while right - left > 1:
    mid = (right + left) // 2
    Next = [-1] * N
    Size = [-1] * N
    ri = 0
    sum = 0
    for le in range(N):
        while ri < N*2 and sum < mid:
            sum += accumulations[ri]
            ri+=1
        if sum >= mid:
            Next[le] = ri
            Size[le] = sum
        if ri == le:
            ri += 1
        else:
            sum -= accumulations[le]
    is_ok = False
    for i in range(N):
        ni = Next[i]
        if ni == -1:continue
        if Size[i] >= total:continue
        ni %= N
        nni = Next[ni]
        if nni == -1:continue
        if total - Size[i] - Size[ni] >= mid:is_ok = True
    if is_ok:
        left = mid
    else:
        right = mid
print(left)