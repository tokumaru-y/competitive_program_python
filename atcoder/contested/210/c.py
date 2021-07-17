N,K=list(map(int, input().split()))
C=list(map(int, input().split()))
# count = [0] * N
ans = 0
num_count = {}
for i in range(K):
    if num_count.get(C[i]) is not None:
        num_count[C[i]] += 1
    else:
        num_count[C[i]] = 1
        ans += 1
tmp = ans
for i in range(K,N):
    leave = C[i-K]
    num_count[leave] -= 1
    if num_count[leave] == 0:
        tmp -=1
    if num_count.get(C[i]) is not None:
        if num_count.get(C[i]) == 0:
            tmp += 1
        num_count[C[i]] += 1
    else:
        num_count[C[i]] = 1
        tmp += 1
    ans = max(ans, tmp)    
print(ans)