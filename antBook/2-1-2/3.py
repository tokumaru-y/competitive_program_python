from collections import deque
import sys
sys.setrecursionlimit(10**9)

N,M=list(map(int, input().split()))
trees = [[] for _ in range(N)]
for _ in range(M):
    u,v=list(map(int, input().split()))
    u,v=u-1,v-1
    trees[u].append(v)
    trees[v].append(u)
ans = 0
passed = [False]*N
def dfs(v, pre):
    global flag
    for t in trees[v]:
        if t == pre:continue
        if passed[t]:
            flag=False
            break
        passed[t]=True
        dfs(t, v)

for i in range(N):
    if passed[i]:continue
    passed[i] = True
    flag = True
    dfs(i, -1)
    if flag:ans += 1
print(ans)