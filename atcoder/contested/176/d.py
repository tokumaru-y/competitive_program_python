from collections import deque
H,W=list(map(int,input().split()))
sh,sw = list(map(lambda x : int(x) - 1,input().split()))
eh, ew = list(map(lambda x : int(x) - 1,input().split()))
grid = [input().rstrip() for _ in range(H)]
cnt = [[float('inf')]* W for _ in range(H) ]
q = deque([])
q.append([0, [sh,sw]])
while len(q) > 0 :
    nc,tmp = q.popleft()
    h,w=tmp
    if cnt[h][w] <= nc:continue
    if h==eh and w==ew:
        print(nc)
        exit()
    cnt[h][w]=nc
    for i in [-1,1]:
        for j in [-1,1]:
            th = h+i
            tw = w+j
            if 0<=th<=H-1 and 0<=tw<=W-1:
                if grid[th][tw] == '.':
                    q.append([nc,[th,tw]])
    for i in range(-2,3):
        for j in range(-2,3):
            if i==0 and j==0:continue
            th = h+i
            tw = w+j
            if 0<=th<=H-1 and 0<=tw<=W-1:
                if cnt[th][tw] <= nc or grid[th][tw] == '#':continue
                q.append([nc+1,[th,tw]])
print(-1)