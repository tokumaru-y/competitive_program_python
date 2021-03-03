import sys
input = sys.stdin.readline
H,W,M=list(map(int,input().split()))
grid = [["."] * W for _ in range(H)]
for _ in range(M):
    h,w=list(map(lambda x : int(x)-1,input().split()))
    grid[h][w]='#'
h_sum = [[0]*(W+1) for _ in range(H+1)]
w_sum = [[0]*(W+1) for _ in range(H+1)]
sum_list = [[0]*W for _ in range(H)]
ans = 0
for h in range(H):
    for w in range(W):
        tmp_sum = h_sum[h-1][w]+w_sum[h][w-1]
        if grid[h][w]=='#':
            tmp_sum+=1
            h_sum[h][w]=h_sum[h-1][w]+1
            w_sum[h][w]=w_sum[h][w-1]+1
        sum_list[h][w] = tmp_sum
        ans = max(ans, tmp_sum)
print(ans)