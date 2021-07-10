N,X=list(map(int, input().split()))
A=list(map(int, input().split()))
ans = 0
for i in range(N):
    if i%2==1:
        ans-=1
    ans+=A[i]
print("Yes" if X-ans>=0 else "No")