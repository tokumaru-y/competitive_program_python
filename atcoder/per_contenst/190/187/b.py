N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
ans=0
XY.sort()
for i in range(N):
    for j in range(i+1,N):
        x1,y1=XY[i]
        x2,y2=XY[j]
        dx,dy=x2-x1,y2-y1
        if -dx <= dy and dy <= dx:ans+=1
print(ans)