N=int(input())
A=list(map(int,input().split()))
A.sort()
ans = A[0]
for a in A[1:]:
    if ans * a>10**18:
        print(-1)
        exit()
    ans *= a
print(ans)