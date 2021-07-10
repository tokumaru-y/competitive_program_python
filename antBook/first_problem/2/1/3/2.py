from collections import deque
H,W,N=list(map(int, input().split()))
grid = [[None] * W for _ in range(H)]
sh,sw =0,0
for i in range(H):
    l = input().rstrip()
    for j in range(W):
        grid[i][j] = l[j]
        if l[j]=="S":
            sh=i
            sw=j
ans = 0
hi=[0,1,0,-1]
wi=[1,0,-1,0]
for target in range(1,N+1):
    passed = [[-1] * W for _ in range(H)]
    passed[sh][sw]=0
    d = deque([[sh,sw]])
    while len(d)>0:
        nh,nw = d.popleft()
        for i in range(4):
            h = nh+hi[i]
            w = nw+wi[i]
            if 0<=h<=H-1 and 0<=w<=W-1 and passed[h][w] == -1 and grid[h][w] != "X":
                passed[h][w] = passed[nh][nw] + 1
                if grid[h][w] == str(target):
                    ans += passed[h][w]
                    sh = h
                    sw = w
                    d.clear()
                    break
                d.append([h,w])
print(ans)
        