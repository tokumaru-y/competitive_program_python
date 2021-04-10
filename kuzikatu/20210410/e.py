from collections import deque
import copy
H,W=list(map(int, input().split()))
grid = [input().rstrip() for _ in range(H)]
pre = [[False] * W for _ in range(H)]
ans = 0
hi = [0,1,0,-1]
wi = [1,0,-1,0]
for i in range(H):
    for j in range(W):
        passed = copy.deepcopy(pre)
        passed[i][j] = True
        origin_black = True if grid[i][j] == '#' else False
        d = deque([[i,j,origin_black]])
        while len(d) > 0:
            nh,nw,is_black = d.popleft()
            for k in range(4):
                h = nh+hi[k]
                w = nw+wi[k]
                if 0<=h<=H-1 and 0<=w<=W-1:
                    if passed[h][w]:continue
                    if is_black and grid[h][w] == '#':continue
                    if not is_black and grid[h][w] == '.':continue
                    if origin_black and grid[h][w] == '.':ans+=1
                    if not origin_black and grid[h][w] == '#':ans+=1
                    passed[h][w] = True
                    d.append([h,w,grid[h][w]=='#'])
        pre[i][j] = True
print(ans)
