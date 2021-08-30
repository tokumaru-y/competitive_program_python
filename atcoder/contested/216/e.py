N,K=list(map(int, input().split()))
A=list(map(int,input().split()))
A.sort(reverse=True)
A += [0]
ans = 0
for i in range(N):
    dif = A[i] - A[i+1]
    cnt = dif*(i+1)
    if cnt <= K:
        K-= cnt
        ans += (dif*(A[i] + A[i]-dif+1)//2)*(i+1)
    else:
        x = K // (i+1)
        y = K % (i+1)
        ans += x*(A[i] + A[i]-x+1)//2 * (i+1)
        ans += (A[i] - x) * y
        K=0
print(ans)