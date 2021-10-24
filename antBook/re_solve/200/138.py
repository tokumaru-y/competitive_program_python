# https://atcoder.jp/contests/arc064/tasks/arc064_a
N,x= list(map(int, input().split()))
A=list(map(int, input().split()))
ans = 0
sum = 0
for i in range(N):
    sum += A[i]
    if sum > x:
        remove_cnt = sum - x
        A[i] = 0 if remove_cnt > A[i] else A[i] - remove_cnt
        sum = A[i]
        ans += remove_cnt
    else:
        sum -= A[i-1] if i >= 1 else 0
print(ans)