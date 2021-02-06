H,W=list(map(int,input().split()))
grid=[input().rstrip() for _ in range(H)]
ans=0
dirc=[[0,0],[0,1],[1,0],[1,1]]
for h in range(H-1):
    for w in range(W-1):
        tmp=[]
        for d in dirc:
            nh=h+d[0]
            nw=w+d[1]
            tmp.append(grid[nh][nw])
        cnt = tmp.count("#")
        if cnt==1 or cnt==3:
            ans+=1
print(ans)