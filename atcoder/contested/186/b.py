h,w=list(map(int,input().split()))
min_num=float('inf')
sum_num=0
grids=[list(map(int,input().split())) for _ in range(h)]
for i in range(h):
    for j in range(w):
        sum_num+=grids[i][j]
        min_num=min(min_num,grids[i][j])
print(sum_num - (min_num * h * w))