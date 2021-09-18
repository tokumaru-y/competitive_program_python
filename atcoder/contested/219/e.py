from collections import deque
grid = []
for _ in range(4):
    l = list(map(int, input().split()))
    grid.append(l)
cnt = [[0] * 4 for _ in range(4)]
total = 0
tmp =[[0] * 4 for _ in range(4)]
l = deque([[0,0]])
passed = [[False] * 4 for _ in range(4)]
cnt[0][0]=1
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for x in range(4):
    for y in range(4):
        if grid[x][y]==1:
            cnt = [[0] * 4 for _ in range(4)]
            passed = [[False] * 4 for _ in range(4)]
            l=deque([[x,y]])
            cnt[x][y]=1
            while len(l)>0:
                nx,ny = l.popleft()
                cnt[nx][ny] += 1
                total += cnt[nx][ny]
                passed[nx][ny] = True
                for i in range(4):
                    x = nx+dx[i]
                    y = ny+dy[i]
                    if not (0<=x<=3 and 0<=y<=3):continue
                    if passed[x][y] or grid[x][y]==1:continue
                    cnt[x][y]+=cnt[nx][ny]
                    l.append([x,y])
cnt = [[0] * 4 for _ in range(4)]
passed = [[False] * 4 for _ in range(4)]
for x in range(4):
    for y in range(4):
        if grid[x][y]==0:
            cnt = [[0] * 4 for _ in range(4)]
            passed = [[False] * 4 for _ in range(4)]
            l=deque([[x,y]])
            cnt[x][y]=1
            while len(l)>0:
                nx,ny = l.popleft()
                cnt[nx][ny] += 1
                total -= cnt[nx][ny]
                passed[nx][ny] = True
                for i in range(4):
                    x = nx+dx[i]
                    y = ny+dy[i]
                    if not (0<=x<=3 and 0<=y<=3):continue
                    if passed[x][y] or grid[x][y]==1:continue
                    cnt[x][y]+=cnt[nx][ny]
                    l.append([x,y])

print(total)