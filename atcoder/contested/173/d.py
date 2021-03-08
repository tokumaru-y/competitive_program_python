N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
min_num=A[-1]
ans = A[0]
index = 1
for i in range(2,N):
    ans+=A[index]
    if i%2==1:index+=1
print(ans)