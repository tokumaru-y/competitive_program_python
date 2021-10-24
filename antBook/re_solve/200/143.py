# https://atcoder.jp/contests/abc018/tasks/abc018_4
N,M,P,Q,R = list(map(int, input().split()))
XYZ = [list(map(int, input().split())) for _ in range(R)]
ans = 0
# cnt_table[i][j]:=i番目の女子が選ばれた際のj番目の男子の幸福度の合計
cnt_table = [[0] * M for _ in range(N)]
for x,y,z in XYZ:
    x-=1
    y-=1
    cnt_table[x][y]+=z
for bit in range(1<<N):
    tmp_cnt = [0] * M
    g_cnt = 0
    for i in range(N):
        if bit & (1<<i):
            g_cnt+=1
            if g_cnt > P:break
            for j in range(M):
                tmp_cnt[j]+=cnt_table[i][j]
    if g_cnt > P:continue
    tmp_cnt.sort(reverse=True)
    ans = max(ans, sum(tmp_cnt[:Q]))
print(ans)