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
# これだと、以下のテストケースで1を返してしまう。
# 4 4
# 1 2
# 1 3
# 1 4
# 3 4
# 要するに根からではない場合に、先にTrueを返してしまったりしてしまう。
def dfs(v, pre):
    for t in trees[v]:
        if t == pre:continue
        if passed[t]:return False
        passed[t]=True
        return dfs(t, v)
    return True
for i in range(N):
    if passed[i]:continue
    passed[i] = True
    if dfs(i, -1):
        ans += 1
print(ans)