n=int(input())
grids=[list(map(int,input().split())) for _ in range(n)]

ans=0
for i in range(n):
    for j in range(i+1,n):
        t = (grids[j][1] - grids[i][1]) / (grids[j][0] - grids[i][0])
        if -1 <= t <= 1:
            ans+=1

print(ans)