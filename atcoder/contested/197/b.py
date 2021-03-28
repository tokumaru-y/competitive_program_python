H,W,X,Y=list(map(int,input().split()))
grid = [input().rstrip() for _ in range(H)]
ans = 0
tmp = 0
for y in range(W):
    if grid[X-1][y] == '.':
        tmp+=1
    else:
        if y >= Y-1:
            break
        tmp = 0
ans +=tmp
tmp = 0
for x in range(H):
    if grid[x][Y-1] == '.':
        tmp+=1
    else:
        if x >= X-1:
            break
        tmp = 0
ans +=tmp
print(ans-1)