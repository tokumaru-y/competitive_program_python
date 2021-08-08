from heapq import heapify
import heapq


from heapq import heapify,heappush,heappop
H,W=list(map(int, input().split()))
grid=[list(input()) for _ in range(H)]
hh = [[0,0,0]]
heapify(hh)
hi=[0,1,0,-1]
wi=[1,0,-1,0]
passed = [[False] * W for _ in range(H)]
passed[0][0]=True
while True:
    count,h,w=heappop(hh)
    for i in range(4):
        nh = h+hi[i]
        nw = w+wi[i]
        if not(0<=nh<=H-1 and 0<=nw<=W-1) or passed[nh][nw]:continue
        passed[nh][nw]=True
        if nh == H-1 and nw == W-1:
            print(count)
            exit()
        passed[nh][nw]=True
        if grid[nh][nw] == '.':
            heappush(hh,[count,nh,nw])
        else:
            # 横移動
            if i%2==0:
                if nh>=1:
                    if not passed[nh-1][nw]:
                        if grid[nh-1][nw]!='.':
                            heappush(hh,[count+1,nh-1,nw])
                    if nw + 1 <= W-1 and not passed[nh-1][nw+1]:
                        if grid[nh-1][nw+1]!='.':
                            heappush(hh,[count+1,nh-1,nw+1])
                heappush(hh, [count+1,nh,nw])
                if nw + 1 <= W-1 and grid[nh][nw+1]!='.':
                    heappush(hh, [count+1,nh,nw+1])
                if nh <= H-2:
                    if not passed[nh+1][nw] and grid[nh+1][nw]!=".":
                        heappush(hh, [count+1,nh+1,nw])
                    if nw + 1 <= W-1 and not passed[nh+1][nw+1] and grid[nh+1][nw+1]!='.':
                        heappush(hh, [count+1,nh+1,nw+1])
            else:
                if nw>=1:
                    if not passed[nh][nw-1] and grid[nh][nw-1]:heappush(hh,[count+1,nh,nw-1])
                    if nh + 1 <= H-1 and not passed[nh+1][nw-1] and grid[nh+1][nw-1] != '.':
                        heappush(hh,[count+1,nh+1,nw-1])
                heappush(hh, [count+1,nh,nw])
                if nh + 1 <= H-1 and not passed[nh+1][nw] and grid[nh+1][nw]!='.':
                    heappush(hh, [count+1,nh+1,nw])
                if nw <= W-2:
                    if not passed[nh][nw+1] and grid[nh][nw+1]!='.':
                        heappush(hh, [count+1,nh,nw+1])
                    if nh + 1 <= H-1 and passed[nh+1][nw+1] and grid[nh+1][nw+1]!='.':
                        heappush(hh, [count+1,nh+1,nw+1])
