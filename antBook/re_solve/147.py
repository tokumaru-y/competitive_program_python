# https://atcoder.jp/contests/tdpc/tasks/tdpc_dice
N,D=list(map(int, input().split()))
two, three, five = 61, 41, 26
dp =[[[[0] * five for _ in range(three)] for _ in range(two)] for _ in range(N+1)]
dp[0][0][0][0]=1
cnt_table = [0,0,0]
for _idx, i in enumerate([2,3,5]):
    while D%i==0:
        cnt_table[_idx]+=1
        D//=i
if D!=1:
    print(0)
    exit()
a,b,c=cnt_table
d1=[0,1,0,2,0,1]
d2=[0,0,1,0,0,1]
d3=[0,0,0,0,1,0]
for idx in range(N):
    for t in reversed(range(a+1)):
        for th in reversed(range(b+1)):
            for f in reversed(range(c+1)):
                for i in range(6):
                    x=min(a,d1[i]+t)
                    y=min(b,d2[i]+th)
                    z=min(c,d3[i]+f)
                    dp[idx+1][x][y][z]+=dp[idx][t][th][f]/6
print(dp[N][a][b][c])