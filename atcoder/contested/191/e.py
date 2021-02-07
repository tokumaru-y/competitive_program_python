import heapq
N,M=list(map(int,input().split()))
dp=[[float('inf')] * N for _ in range(N)]
roots=[{} for _ in range(N)]
for _ in range(M):
    a,b,c=list(map(int,input().split()))
    a-=1
    b-=1
    roots[a][b]= c if b not in roots[a] else min(c,roots[a][b])
for i in range(N):
    q=[[0,i]]
    heapq.heapify(q)
    passed=[False]*N
    passed[i]=True
    while len(q) >0 :
        h=heapq.heappop(q)
        cnt,top=h
        if len(roots[top]) > 0:
            for k,v in roots[top].items():
                if not passed[k]:
                    passed[k]=True
                    sum_num=cnt+v
                    dp[i][k]=sum_num
                    heapq.heappush(q,[sum_num,top])
    print(passed,i)
print(dp)
print(roots)
for i in range(N):
    tmp=float('inf') if dp[i][i] != float('inf') else dp[i][i]
    for j in range(N):
        tmp1=dp[i][j]+dp[j][i]
        tmp=min(tmp,tmp1)
    ans[i]=min(ans[i],tmp)
print(*ans,sep='\n')     

