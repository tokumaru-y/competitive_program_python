N=int(input())
ans=float('inf')
for _ in range(N):
    x,y,z=list(map(int,input().split()))
    d = z-x
    if d > 0:
        ans=min(ans, y)
print(ans if ans != float('inf') else -1)