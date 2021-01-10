import copy
r,c=list(map(int,input().split()))
grid=[list(map(int,input().split())) for _ in range(r)]
ans=0
for bit in range(1<<r):
    tmp_grid=copy.deepcopy(grid)
    for j in range(r):
        if bit & 1<<j:
            for k in range(c):
                tmp_grid[j][k] = 1 - tmp_grid[j][k]
    tmp_cnt=0
    for w in range(c):
        num=0
        for h in range(r):
            if tmp_grid[h][w]==1:
                num+=1
        tmp_cnt+=max(num,r-num)
    ans=max(ans,tmp_cnt)
print(ans)