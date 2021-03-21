N=int(input())
A=list(map(int,input().split()))
highs = {}
for i in range(N):
    a = i+1
    b = A[i]
    if a+b in highs:
        highs[a+b]+=1
    else:
        highs[a+b]=1
ans = 0
for i in range(N):
    a = i+1
    b = A[i]
    if a - b in highs:
        ans += highs[a-b]
print(ans)