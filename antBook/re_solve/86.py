from collections import deque
import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int, input().split()))
graph = [[-1] * 2000 for _ in range(2000)]
tops = [[] for _ in range(N)]
A=[-1]*M
B=[-1]*M
colors = [-1] * M
for i in range(M):
    a,b,c=input().split()
    a=int(a)-1
    b=int(b)-1
    tops[a].append(b)
    tops[b].append(a)
    graph[a][b]=i
    graph[b][a]=i
    colors[i] = int(c=='r')
vis=[False]*M
lenght=[-1]*M
def dfs(t,c,len):
    if lenght[t] < 0:
        lenght[t] = len
    elif abs(len - lenght[t])%2 == 1:
        print("Yes")
        exit()
    for nt in tops[t]:
        g_id = graph[t][nt]
        if vis[g_id]:continue
        if colors[g_id] == c:
            vis[g_id]=True
            dfs(nt, abs(c-1), len+1)
for i in range(N):
    for c in range(2):
        vis = [False]*M
        lenght=[-1]*N
        dfs(i,c,0)
        if all(vis):
            print("Yes")
            exit()
print("No")