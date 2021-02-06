import sys
sys.setrecursionlimit(10000)
N,M=list(map(int,input().split()))
graph = [[] for _ in range(N)]
costs=[[float('inf')]*N for _ in range(N)]
ans=[0]*N
for _ in range(M):
    a,b,c=list(map(int,input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    costs[a][b]=min(costs[a][b],c)

def can_return(ll,origin,past,cnt):
    res = float('inf')
    if len(ll) > 0:
        for l in ll:
            if l==origin:
                return cnt+costs[past][l]
                break
            if passed[l]:continue
            passed[l]=True
            tmp = can_return(graph[l],origin,l,cnt+costs[past][l])
            res = min(res,tmp)
    return res
for i in range(N):
    passed=[False]*N
    passed[i]=True
    res = can_return(graph[i],i,i,0)
    ans[i]=res if res != float("inf") else -1

print(*ans,sep='\n')