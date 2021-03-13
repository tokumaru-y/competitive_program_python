import bisect
N,M,K=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sum_a = [0] * (N+1)
sum_b = [0] * (M+1)
for i in range(N):
    sum_a[i+1] = sum_a[i]+A[i]
for i in range(M):
    sum_b[i+1] = sum_b[i]+B[i]

ans = 0
for i in range(N+1):
    tmp = i
    left = K - sum_a[i]
    if left < 0:
        continue
    ind = bisect.bisect_right(sum_b, left)
    ind -= 1
    ans = max(ans, ind+tmp)
print(ans)