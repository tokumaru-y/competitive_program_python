from heapq import heappush, heapify, heappop
H,W = list(map(int, input().split()))
grid = []
sh,sw=0,0
eh,ew=0,0
for h in range(H):
    inline = list(input())
    grid.append(inline)
    for w in range(W):
        if grid[h][w] == 's':
            sh = h
            sw = w
        if grid[h][w] == 'g':
            eh = h
            ew = w
h = [[0,[sh,sw]]]
heapify(h)
passed = [[False] * W for _ in range(H)]
h_ind_list = [0,1,0,-1]
w_ind_list = [1,0,-1,0]
passed[sh][sw]=True
while len(h) > 0:
    time,place = heappop(h)
    oh,ow = place
    for i in range(4):
        nh = oh + h_ind_list[i]
        nw = ow + w_ind_list[i]
        if not(0<=nh<H and 0<=nw<W) or passed[nh][nw]:continue
        if nh == eh and nw == ew:
            print("YES")
            exit()
        if grid[nh][nw] == '#':
            tmp_time = time+1
            if tmp_time >=3:continue
            heappush(h, [tmp_time,[nh,nw]])
        else:
            heappush(h, [time, [nh,nw]])
        passed[nh][nw]=True
print("NO")