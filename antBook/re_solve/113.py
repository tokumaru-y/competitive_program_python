# https://atcoder.jp/contests/arc064/tasks/arc064_a
N,X=list(map(int, input().split()))
A=list(map(int, input().split()))
ans = 0
sum_num = A[0]
for i in range(1,N):
    sum_num += A[i]
    if sum_num > X:
        ans += sum_num - X
        if A[i] >= sum_num - X:
            A[i] -= sum_num - X
            sum_num = A[i]
        else:
            A[i] = 0
            sum_num = 0
    else:
        sum_num -= A[i-1]
print(ans)
