import sys
input = sys.stdin.readline
H,W,M=list(map(int,input().split()))
grid = [["."] * W for _ in range(H)]
h_cnt=[0]*H
w_cnt=[0]*W
for _ in range(M):
    h,w=list(map(lambda x : int(x)-1,input().split()))
    grid[h][w]='#'
    h_cnt[h]+=1
    w_cnt[w]+=1
h_max=max(h_cnt)
h_list = list(filter(lambda x : h_cnt[x]==h_max, range(H)))
w_max=max(w_cnt)
w_list = list(filter(lambda x : w_cnt[x]==w_max, range(W)))
ans = h_max+w_max-1
for h in h_list:
    for w in w_list:
        if grid[h][w] != '#':
            ans += 1
            print(ans)
            exit()
print(ans)