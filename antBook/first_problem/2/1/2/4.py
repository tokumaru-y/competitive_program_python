from collections import deque
while True:
    W,H = list(map(int ,input().split()))
    if H == 0 and W == 0:break
    grid = [list(map(int,input().split())) for _ in range(H)]
    ans = 0
    passed = [[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1 and not passed[i][j]:
                passed[i][j]=True
                d = deque([[i,j]])
                while len(d) > 0:
                    h,w = d.popleft()
                    for hh in [-1,0,1]:
                        for ww in [-1,0,1]:
                            th=h+hh
                            tw=w+ww
                            if 0<=th<=H-1 and 0<=tw<=W-1 and grid[th][tw] == 1 and not passed[th][tw]:
                                passed[th][tw] = True
                                d.append([th,tw])
                ans+=1
    print(ans)