H,W=list(map(int, input().split()))
grid = []
for _ in range(H):
    grid.append(list(map(int, input().split())))
for h in range(H):
    for w in range(W):
        for x in range(h+1, H):
            for y in range(w+1, W):
                if grid[h][w] + grid[x][y] > grid[x][w] + grid[h][y]:
                    print("No")
                    exit()
print("Yes")