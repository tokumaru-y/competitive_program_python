from collections import deque
H,W=list(map(int, input().split()))
grid=[[-1]*W for _ in range(H)]
sh,sw,eh,ew=0,0,0,0
for h in range(H):
    ll = input().rstrip()
    for w in range(W):
        grid[h][w] = ll[w]
        if ll[w] == 's':
            sh,sw=h,w
        elif ll[w] == 'g':
            eh,ew=h,w

d = deque([])
d.append([sh,sw])
passed = [[False]*W for _ in range(H)]
passed[sh][sw]=True
hh = [1,0,-1,0]
ww = [0,1,0,-1]
while len(d)>0:
    nh,nw = d.popleft()
    for i in range(4):
        h,w = nh+hh[i],nw+ww[i]
        if 0<=h<=H-1 and 0<=w<=W-1:
            if passed[h][w] or grid[h][w]=='#':continue
            passed[h][w] = True
            if h==eh and w==ew:
                print("Yes")
                exit()
            else:
                d.append([h,w])
print("No")