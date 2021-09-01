from collections import deque
H,W=list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
h_dir = [0,1,0,-1]
w_dir = [1,0,-1,0]
hq = deque([[0,0,0]])
passed = [[False]*W for _ in range(H)]
while True:
    cnt,nh,nw = hq.popleft()
    passed[nh][nw]=True
    for i in range(4):
        h,w = h_dir[i]+nh, w_dir[i]+nw
        if not(0<=h<=H-1 and 0<=w<=W-1):continue
        if passed[h][w]:continue
        if h == H-1 and w == W-1:
            print(cnt)
            exit()
        if grid[h][w] == '.' and not passed[h][w]:
            hq.appendleft([cnt,h,w])
        else:
            if i == 0:
                for s in [-1,0,1]:
                    if 0<=h+s<=H-1:
                        if not passed[h+s][w]:hq.append([cnt+1,h+s,w])
                        if w+1<=W-1 and not passed[h+s][w+1]:
                            hq.append([cnt+1,h+s,w+1])
            elif i == 1:
                for s in [-1,0,1]:
                    if 0<=w+s<=W-1:
                        if not passed[h][w+s]:hq.append([cnt+1,h,w+s])
                        if h+1<=H-1 and not passed[h+1][w+s]:
                            hq.append([cnt+1,h+1,w+s])
            elif i == 2:
                for s in [-1,0,1]:
                    if 0<=h+s<=H-1: 
                        if not passed[h+s][w]:hq.append([cnt+1,h+s,w])
                        if w-1>=0 and not passed[h+s][w-1]:
                            hq.append([cnt+1,h+s,w-1])
            elif i == 3:
                for s in [-1,0,1]:
                    if 0<=w+s<=W-1:
                        if not passed[h][w+s]:hq.append([cnt+1,h,w+s])
                        if h-1>=0 and not passed[h-1][w+s]:
                            hq.append([cnt+1,h-1,w+s])
