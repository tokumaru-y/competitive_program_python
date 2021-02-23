N=int(input())
ans=0
for _ in range(N):
    a,b=list(map(int,input().split()))
    ans+=(b-a+1)*(a+b)//2
print(ans)