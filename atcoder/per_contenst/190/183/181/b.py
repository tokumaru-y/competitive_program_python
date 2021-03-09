n=int(input())
ans=0
for _ in range(n):
    a,b=list(map(int,input().split()))
    ans+=(b*(b+1) - (a-1)*a)//2
print(ans)