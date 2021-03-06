import sys
input = sys.stdin.readline
N=int(input())
ans = float('inf')
AB=[list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        a,b=AB[i]
        c,d=AB[j]
        if i==j:
            ans=min(ans,a+b)
        else:
            ans=min(ans,min(max(a,d),max(b,c)))
print(ans)