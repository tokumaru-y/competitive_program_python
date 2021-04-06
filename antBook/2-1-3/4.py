from collections import deque
H,W=list(map(int, input().split()))
grid=[[None]*W for _ in range(H)]
d = deque([])
passed = [[False] * W for _ in range(H)]
for i in range(H):
    l = input().rstrip()
    for j in range(W): 
        grid[i][j] = l[j]
        if l[j] == '#':
            d.append([i,j,0])
            passed[i][j] = True
ans = 0
hi=[1,0,-1,0]
wi=[0,1,0,-1]
while len(d) > 0:
    nh,nw,cnt =d.popleft()
    for i in range(4):
        h=nh+hi[i]
        w=nw+wi[i]
        if 0<=h<=H-1 and 0<=w<=W-1 and not passed[h][w] and grid[h][w] != '#':
            passed[h][w] = True
            ans = max(ans,cnt+1)
            d.append([h,w,cnt+1])
print(ans)