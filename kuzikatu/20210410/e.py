from collections import deque
import copy
H,W=list(map(int, input().split()))
grid = [input().rstrip() for _ in range(H)]
passed = [[False] * W for _ in range(H)]
ans = 0
hi = [1,0,-1,0]
wi = [0,1,0,-1]
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':continue
        if passed[i][j]:continue
        passed[i][j] = True
        d = deque([[i,j,True]])
        p_list = [[i,j]]
        cnt = 0
        while len(d) > 0:
            nh, nw, is_black = d.popleft()
            for k in range(4):
                h,w = nh+hi[k], nw+wi[k]
                if 0<=h<=H-1 and 0<=w<=W-1:
                    if passed[h][w]:continue
                    if is_black:
                        if grid[h][w] =='#':continue
                        else:cnt+=1
                    else:
                        if grid[h][w] == '#':
                            p_list.append([h,w])
                        else:continue
                    passed[h][w] = True
                    d.append([h,w,grid[h][w] == '#'])
        ans+=cnt*len(p_list)
print(ans)