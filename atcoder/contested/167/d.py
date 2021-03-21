N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
dubling = [[0] * N for _ in range(60)]
for i in range(N):
    dubling[0][i] = A[i] - 1

for i in range(59):
    for j in range(N):
        dubling[i+1][j] = dubling[i][dubling[i][j]]
ans = 0
for i in range(60):
    if K & (1<<i):
        ans = dubling[i][ans]
print(ans+1)