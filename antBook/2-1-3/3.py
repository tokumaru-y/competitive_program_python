from collections import deque
H,W=list(map(int, input().split()))
grid = [[None] * W for _ in range(H)]
black_cnt = 0
for i in range(H):
    l = input().rstrip()
    for j in range(W):
        grid[i][j] = l[j]
        if grid[i][j] == '#':black_cnt+=1
d = deque([[0,0]])
passed = [[-1] * W for _ in range(H)]
passed[0][0]=0
hi = [1,0,-1,0]
wi = [0,1,0,-1]
while len(d) > 0:
    nh,nw = d.popleft()
    for i in range(4):
        h = nh+hi[i]
        w = nw+wi[i]
        if 0<=h<=H-1 and 0<=w<=W-1 and grid[h][w] != '#' and passed[h][w] == -1:
            passed[h][w] = passed[nh][nw] + 1
            if h==H-1 and w == W-1:
                print(H*W - black_cnt  - 1 - passed[h][w])
                exit()
            d.append([h,w])
print(-1)