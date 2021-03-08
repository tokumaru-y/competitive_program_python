H,W,K=list(map(int,input().split()))
grid=[input().rstrip() for _ in range(H)]
ans = 0
for h in range(1<<H):
    for w in range(1<<W):
        tmp_cnt =0
        for i in range(H):
            for j in range(W):
                if h & 1<<i and w & 1<<j:
                    if grid[i][j]=='#':
                        tmp_cnt+=1
        if tmp_cnt == K:ans+=1
print(ans)