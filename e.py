import sys

sys.setrecursionlimit(10**9)
N=int(input())
S=[input() for _ in range(N)]
indict={}
outdict=[[] for _ in range(N)]
passed=[False]*N
ans = [False]*N
graph = [[] for _ in range(N)]
for i in range(N):
    if S[i][:3] in indict:
        indict[S[i][:3]].append(i)
    else:
        indict[S[i][:3]] = [i]
    outdict[i] = S[i][-3:]
def dfs(top):
    passed[top]=True
    instr = outdict[top]
    if indict.get(instr,None) is None:
        return
    for nx_i in indict[instr]:
        if passed[nx_i]:
            graph[top].append(nx_i)
            continue
        graph[top].append(nx_i)
        dfs(nx_i)
for i in range(N):
    if passed[i]:continue
    dfs(i)
passed=[False]*N
deepth = [0] * N
def dfs2(top,list):
    passed[top]=True
    list.append(top)
    if len(graph[top]) == 0:
        deepth[top]=1
        return 1
    for nx in graph[top]:
        if passed[nx]:
            if nx in list:
                deepth[nx]=float("inf")
                return float("inf")
            else:
                return deepth[nx]+1
        deepth[nx] = dfs2(nx,list)
for i in range(N):
    if passed[i]:continue
    dfs2(i,[i])
for d in deepth:
    if d==float("inf"):
        print("Draw")
    elif d%2==1:
        print("Takahashi")
    else:
        print("Aoki")