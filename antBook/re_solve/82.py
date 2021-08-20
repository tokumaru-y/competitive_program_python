import sys
sys.setrecursionlimit(10**9)
N=int(input())
graph=[[] for _ in range(N)]
for _ in range(N-1):
    u,v,w = list(map(int, input().split()))
    u-=1
    v-=1
    graph[u].append([v,w])
    graph[v].append([u,w])
ans = [-1] * N
def dfs(t,c):
    for nt, nw in graph[t]:
        if ans[nt] > -1:continue
        if nw%2==0:
            ans[nt]=c
            dfs(nt, c)
        else:
            ans[nt]=abs(c-1)
            dfs(nt,abs(c-1))
ans[0]=0
dfs(0,0)
print(*ans, sep="\n")