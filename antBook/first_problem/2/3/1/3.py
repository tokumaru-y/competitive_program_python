N,D=list(map(int, input().split()))
# 2**60, 3**40, 5**30
div_num = [2,3,5]
div_count = [0,0,0]
for index, d in enumerate(div_num):
    while D%d==0:
        D//=d
        div_count[index] += 1
c2,c3,c5 = div_count
dp=[[[[0] * (c2+1) for _ in range(c3+1)] for _ in range(c5+1)] for _ in range(N+1)]
if D!=1:
    print(0)
    exit()
d1 = [0,1,0,2,0,1]
d2 = [0,0,1,0,0,1]
d3 = [0,0,0,0,1,0]
dp[0][0][0][0] = 1
for n in range(N):
    for i in range(c2+1):
        for j in range(c3+1):
            for k in range(c5+1):
                for d in range(6):
                    nx = min(c2, i+d1[d])
                    ny = min(c3, j+d2[d])
                    nz = min(c5, k+d3[d])
                    dp[n+1][nz][ny][nx] += dp[n][k][j][i]/6
print(dp[N][c5][c3][c2])