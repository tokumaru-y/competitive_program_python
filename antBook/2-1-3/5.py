from heapq import heapify,heappush, heappop
H,W=list(map(int, input().split()))
grid=[[None] * W for _ in range(H)]
sh,sw=0,0
eh,ew=0,0
for i in range(H):
    l = input().rstrip()
    for j in range(W):
        grid[i][j] = l[j]
        if l[j] == 's':
            sh=i
            sw=j
        if l[j] == 'g':
            eh=i
            ew=j

d = [[0,sh,sw]]
heapify(d)
passed = [[False] * W for _ in range(H)]
passed[sh][sw] = True
while len(d) > 0:
    cnt,nh,nw = heappop(d)
    for i,j in zip([0,1,0,-1],[1,0,-1,0]):
        h = nh+i
        w = nw+j
        ncnt = cnt
        if 0<=h<=H-1 and 0<=w<=W-1 and not passed[h][w]:
            if h == eh and w == ew:
                print("YES")
                exit()
            if grid[h][w] == '#':
                ncnt+=1
                if ncnt > 2:continue
            passed[h][w] = True
            heappush(d, [ncnt, h, w])
print("NO")