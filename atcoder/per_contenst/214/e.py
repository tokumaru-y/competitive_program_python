from collections import deque
H,W=list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
h_dir = [0,1,0,-1]
w_dir = [1,0,-1,0]
hq = deque([[0,0,0]])
cnt_grid = [[float("inf")]*W for _ in range(H)]
cnt_grid[0][0]=0
break_dir = [-1,0,1]
while True:
    cnt,nh,nw = hq.popleft()
    if nh==H-1 and nw==W-1:
        print(cnt)
        exit()
    for i in range(4):
        h,w = h_dir[i]+nh, w_dir[i]+nw
        if not(0<=h<=H-1 and 0<=w<=W-1):continue
        if cnt_grid[h][w] <= cnt:continue
        if grid[h][w] == '.':
            hq.appendleft([cnt,h,w])
            cnt_grid[h][w]=cnt
        else:
            for a in range(3):
                for b in range(3):
                    th = h+break_dir[a]
                    tw = w+break_dir[b]
                    if not(0<=th<=H-1 and 0<=tw<=W-1):continue
                    if cnt_grid[th][tw] <= cnt+1:continue
                    hq.append([cnt+1,th,tw])
                    cnt_grid[th][tw]=cnt+1