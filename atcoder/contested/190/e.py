import sys
from collections import deque
input = sys.stdin.readline()
N,M=list(map(int,input().split()))
edges = [[None] * N]
for _ in range(M):
    a,b = list(map(int,input().split()))
    a,b=a-1,b-1
    edges[a].append(b)
    edges[b].append(a)
K = int(input())
C = list(map(lambda x : int(x)-1,input().split()))

ans = float('inf')

def bfs_return_list(t):
    res = [float('inf') * N for _ in range(N)]
    res[t][t]=1
    q = deque([])
    q.append([t,t])
    while len(q) > 0:
        nt,bt = q.popleft()
        if len(C[nt])==0:continue
        for l in range(C[nt]):
            if res[t][l] != float('inf'):continue
            res[t][l]=min(res[t][bt]+1,res[t][l])
            q.append([l,nt])
    return res

# 再起
def search(t):

for i in range(N):
    cnt_list = bfs_return_list(i)
    tmp_sum=0
    search(i)
    ans=min(ans, tmp)
print(ans if ans != float('inf') else -1)
        