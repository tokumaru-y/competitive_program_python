N=int(input())
XYZ=[list(map(int,input().split())) for _ in range(N)]
dp=[[float('inf')]*N for _ in range(1<<N)]
dp[1]=0
