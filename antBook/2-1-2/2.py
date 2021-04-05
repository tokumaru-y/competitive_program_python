from collections import deque
grid = [['']*10 for _ in range(10)]
for h in range(10):
    l = input().rstrip()
    for w in range(10):
        grid[h][w] = l[w]
sh = [1,0,-1,0]
sw = [0,1,0,-1]
for i in range(10):
    for j in range(10):
        d = deque([[i,j]])
        passed = [[False] * 10 for _ in range(10)]
        passed[i][j]=True
        while len(d) > 0:
            nh,nw = d.popleft()
            for k in range(4):
                h,w=nh+sh[k], nw+sw[k]
                if 0<=h<=9 and 0<=w<=9:
                    if passed[h][w] or grid[h][w] == 'x':continue
                    passed[h][w] = True
                    d.append([h,w])
        flag = True
        for a in range(10):
            for b in range(10):
                if grid[a][b]=='o':
                    if not passed[a][b]:
                        flag = False
                        break
        if flag:
            print("YES")
            exit()
print("NO")