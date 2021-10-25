# https://atcoder.jp/contests/joi2010yo/tasks/joi2010yo_d
N=int(input())
K=int(input())
LL = [int(input()) for _ in range(N)]
seen = [False] * (10**8+1)
used = [False] * N
import sys
sys.setrecursionlimit(10**9)
def dfs(tmp_str,used, cnt):
    if cnt == K:
        seen[int(tmp_str)] = True
        return
    for i in range(N):
        if used[i]:continue
        used[i] = True
        dfs(tmp_str+str(LL[i]), used, cnt+1)
        used[i] = False
for i in range(N):
    used[i] = True
    dfs(str(LL[i]), used, 1)
    used[i] = False
ans = 0
for i in range(len(seen)):
    if seen[i]:
        ans+=1
print(ans)