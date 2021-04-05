from collections import deque
H,W=list(map(int, input().split()))
grid = [[''] * W for _ in range(H)]
for i in range(H):
    l = input().rstrip()
    for j in range(W):
        grid[i][j] = l[j]
ans = 0
hd=[1,0,-1,0]
wd=[0,1,0,-1]
for h in range(H):
    for w in range(W):
        if grid[h][w]=='#':continue
        cnt_table = [[-1]*W for _ in range(H)]
        d = deque([[h,w]])
        cnt_table[h][w] = 0
        cnt_max = 0
        while len(d) > 0:
            nh,nw = d.popleft()
            for i in range(4):
                hh = nh+hd[i]
                ww = nw+wd[i]
                if 0<=hh<=H-1 and 0<=ww<=W-1 and cnt_table[hh][ww]==-1 and grid[hh][ww]=='.':
                    cnt_table[hh][ww] = cnt_table[nh][nw] + 1
                    cnt_max = max(cnt_table[hh][ww],cnt_max)
                    # print([nh,nw],h,w,hh,ww,cnt_table,cnt_max)
                    d.append([hh,ww])
        ans = max(ans, cnt_max)
print(ans)