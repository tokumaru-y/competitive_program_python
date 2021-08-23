from collections import deque
import sys
sys.setrecursionlimit(10**9)
N,M=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=input().split()
    a=int(a)-1
    b=int(b)-1
    graph[a].append([b,int(c=='r')])
    graph[b].append([a,int(c=='r')])
vis=[False]*N
lenght=[-1]*N
def dfs(t,c,len):
    if lenght[t] < 0:
        lenght[t] = len
    elif abs(len - lenght[t])%2 == 1:
        print("Yes")
        exit()
    for nt,nc in graph[t]:
        if vis[nt]:continue
        if nc == c:
            vis[nt]=True
            dfs(nt,abs(nc-1),len+1)
    print(vis,lenght)
for i in range(N):
    for c in range(2):
        vis = [False]*N
        lenght=[-1]*N
        vis[i]=True
        dfs(i,c,0)
        if all(vis):
            print("Yes")
            exit()
print("No")