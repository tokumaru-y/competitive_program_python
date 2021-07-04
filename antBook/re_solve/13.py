import sys
sys.setrecursionlimit(10**6)
N=int(input())
A=[int(input()) for _ in range(N)]
type = [-1] * N
graph = [-1] * N
for i in range(N):
    graph[i] = A[i]-1

def dfs(x,t, cnt):
    type[x] = t
    nx = graph[x]
    if cnt > N:
        if t == type[nx]:return False
        return True
    if type[x] == type[nx]:
        return False
    return dfs(nx, abs(t-1), cnt+1)
is_bin=dfs(0,0, 0)
b,w =0,0
for t in type:
    if t==0:
        b+=1
    else: 
        w+=1
if is_bin:
    print(max(b,w))
else:
    print(-1)
