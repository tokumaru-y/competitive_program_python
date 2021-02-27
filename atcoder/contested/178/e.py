N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
Plist=[]
Mlist=[]
for x,y in XY:
    Plist.append(x+y)
    Mlist.append(x-y)
Plist.sort()
Mlist.sort()
ans=max(Plist[-1] - Plist[0], Mlist[-1] - Mlist[0])
print(ans)