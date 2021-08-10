N,D=list(map(int, input().split()))
origin = D
div_coount = [0,0,0]
for ind, num in enumerate([2,3,5]):
    while D%num==0:
        div_coount[ind]+=1
        D//=num
if D != 1:
    print(0)
    exit()
a,b,c=div_coount
dp=[[[[0]*(a+1) for _ in range(b+1)] for _ in range(c+1)]for _ in range(N+1)]
dp[0][0][0][0]=1
d1=[0,1,0,2,0,1]
d2=[0,0,1,0,0,1]
d3=[0,0,0,0,1,0]
for n in range(N):
    for i in range(c+1):
        for j in range(b+1):
            for k in range(a+1):
                for m in range(6):
                    ni=min(c, i+d3[m])
                    nj=min(b,j+d2[m])
                    nk=min(a,k+d1[m])
                    dp[n+1][ni][nj][nk]+=dp[n][i][j][k]/6

print(dp[N][c][b][a])