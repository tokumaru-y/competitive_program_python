# https://atcoder.jp/contests/abc054/tasks/abc054_c
N,M=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]
for a,b in AB:
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
ans = 0
import sys
sys.setrecursionlimit(10**9)
seen = [False] * N
seen[0] = True
def dfs(v, seen, cnt):
    if cnt == N:
        global ans
        ans+=1
        return
    for next_v in graph[v]:
        if seen[next_v]:continue
        seen[next_v] = True
        dfs(next_v, seen,cnt+1)
        seen[next_v] = False
dfs(0,seen,1)
print(ans)