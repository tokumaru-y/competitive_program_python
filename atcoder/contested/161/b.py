N,M=list(map(int,input().split()))
A=list(map(int,input().split()))
s = sum(A)
cnt = 0
for a in A:
    if a * 4 * M >= s:
        cnt += 1
print("Yes" if cnt >= M else "No")