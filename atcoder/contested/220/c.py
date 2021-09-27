N=int(input())
A=list(map(int, input().split()))
X = int(input())
a=sum(A)
ans = X//a
X -= a * ans
ans *= N
for i in range(N):
    X -= A[i]
    ans += 1
    if X<0:break
print(ans)