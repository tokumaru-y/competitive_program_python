N=int(input())
X=list(map(int,input().split()))
ans = float('inf')
for i in range(1,101):
    tmp = 0
    for j in range(N):
        tmp += (i-X[j])**2
    ans = min(ans, tmp)
print(ans)