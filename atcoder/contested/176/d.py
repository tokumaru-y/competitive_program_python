from collections import deque
H,W=list(map(int,input().split()))
sh,sw = list(map(lambda x : int(x) - 1,input().split()))
eh, ew = list(map(lambda x : int(x) - 1,input().split()))
grid = [input().rstrip() for _ in range(H)]
cnt = [[float('inf')]* W for _ in range(H) ]
q = deque([[0,[sh,sw]]])
while len(q) > 0 :
    nc,tmp = q.popleft()
    h,w=tmp
    if cnt[h][w] < nc:continue
    cnt[h][w]=nc
    if h==eh and w==ew:
        print(nc)
        exit()
    for i in range(-2,3):
        for j in range(-2,3):
            if i==j and i==0:continue
            th ,tw = h+i,w+j
            if not (0<=th<=H-1 and 0<=tw<=W-1):continue
            if abs(i) + abs(j)>1:
                if cnt[th][tw] > nc+1 and grid[th][tw] == '.':
                    cnt[th][tw]=nc+1
                    q.append([nc+1,[th,tw]])
            else:
                if cnt[th][tw] > nc and grid[th][tw] == '.':
                    cnt[th][tw]=nc
                    q.appendleft([nc,[th,tw]])
print(-1)