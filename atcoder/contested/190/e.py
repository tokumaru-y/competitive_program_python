import sys
from collections import deque
input = sys.stdin.readline
N,M=list(map(int,input().split()))
edges = [[] for _ in range(N)]
for _ in range(M):
    a,b = list(map(int,input().split()))
    a,b=a-1,b-1
    edges[a].append(b)
    edges[b].append(a)
K = int(input())
C = list(map(lambda x : int(x)-1,input().split()))

ans = float('inf')
dp=[[float('inf')] * N for _ in range(1<<N)]
def bfs_return_list(t):
    res = [[float('inf')] * N for _ in range(N)]
    res[t][t]=1
    q = deque([])
    q.append([t,t])
    while len(q) > 0:
        nt,bt = q.popleft()
        if len(edges[nt])==0:continue
        for l in edges[nt]:
            if res[t][l] != float('inf'):continue
            res[t][l]=min(res[t][bt]+1,res[t][l])
            q.append([l,nt])
    return res

# 再起
def search(bit,target):
    if dp[bit][target] != float('inf'):return dp[bit][target]
    res = float('inf')
    for u in C:
        if (bit & 1<<u):continue
        res=min(res,search(bit|1<<u, u) + cnt_list[target][u])
    dp[bit][target]=res
    return res

for i in C:
    cnt_list = bfs_return_list(i)
    tmp_sum=0
    tmp = search(0,i)
    ans=min(ans, tmp)
print(dp)
print(ans if ans != float('inf') else -1)
        