from collections import deque
H,W=list(map(int,input().split()))
sh,sw=list(map(lambda x : int(x)-1, input().split()))
eh,ew=list(map(lambda x : int(x)-1, input().split()))
grid =[input().rstrip() for _ in range(H)]
ans = float('inf')
d = deque([[sh,sw]])
passed = [[-1] * W for _ in range(H)]
passed[sh][sw]=0
hi = [0,1,0,-1]
wi = [1,0,-1,0]
while len(d) > 0:
    nh,nw = d.popleft()
    for i in range(4):
        h = nh+hi[i]
        w = nw+wi[i]
        if 0<=h<=H-1 and 0<=w<=W-1 and passed[h][w] == -1 and grid[h][w] !='#':
            passed[h][w] = passed[nh][nw] + 1
            if h == eh and w == ew:
                print(passed[h][w])
                exit()
            d.append([h,w])
