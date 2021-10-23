N=int(input())
XY=[list(map(int, input().split())) for _ in range(N)] 
ans = 0
for i in range(N):
    x1,y1=XY[i]
    for j in range(i+1,N):
        x2,y2=XY[j]
        for k in range(j+1,N):
            x3,y3=XY[k]
            tmp = [[x1,y1],[x2,y2],[x3,y3]]
            # tmp.sort()
            a,b,c = tmp
            if (b[1] - a[1]) * (c[0]-b[0]) == (c[1]-b[1]) * (b[0] - a[0]):continue
            ans+= 1
print(ans)