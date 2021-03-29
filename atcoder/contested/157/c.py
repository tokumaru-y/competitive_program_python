N,M=list(map(int,input().split()))
ans = [-1] * N
for _ in range(M):
    s,c = list(map(int,input().split()))
    s -=1
    print(ans)
    if ans[s] != -1 and ans[s] != c:
        print(-1)
        exit()
    ans[s] = c
for i in range(N):
    if ans[i] == -1:
        ans[i] = 0

for i in range(1000):
    if i < 10**N:continue
    