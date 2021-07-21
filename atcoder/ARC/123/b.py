from bisect import bisect_left,bisect_right
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
bi = 0
ci = 0
for i in range(N):
    target=A[i]
    while bi <= N-1 and target >= B[bi]:
        bi+=1
    if bi >= N:break
    while ci <= N-1 and B[bi] >= C[ci]:
        ci+=1
    if ci>=N:break
    ans += 1
    bi += 1
    ci += 1
print(ans)