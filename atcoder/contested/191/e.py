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
    for j in range(N):
        if i==j:
            if j in roots[i]:
                dp[i][j]=min(dp[i][j],roots[i][j])
            continue
        q=[]
        passed = [False]*N
        passed[i]=True
        heapq.heapify(q)
        # [cnt, now_top]
        heapq.heappush(q,[0,i])
        tmp = float('inf')
        while len(q) > 0:
            cnt,top = heapq.heappop(q)
            if len(roots[top]) > 0:
                if tmp==float('inf'):tmp=0
                for k,v in roots[top].items():
                    if not passed[k]:
                        passed[k] = True
                        heapq.heappush(q,[cnt+v,k])
                        tmp += cnt+v
        dp[i][j]=tmp
ans=[float('inf') for _ in range(N)]
print(dp)
for i in range(N):
    tmp=float('inf') if dp[i][i] != float('inf') else dp[i][i]
    for j in range(N):
        tmp1=dp[i][j]+dp[j][i]
        tmp=min(tmp,tmp1)
    ans[i]=min(ans[i],tmp)
print(*ans,sep='\n')     

