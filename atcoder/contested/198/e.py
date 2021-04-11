import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())
C=list(map(int, input().split()))
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = list(map(int, input().split()))
    a,b = a-1,b-1
    tree[a].append(b)
    tree[b].append(a)
ans = []
passed = [False] * N
used = [0] * ((10 ** 5)+1)
passed[0] = True
used[C[0]] = 1
def dfs(n):
    for h in tree[n]:
        if passed[h]:continue
        passed[h]=True
        if not used[C[h]]:
            ans.append(h+1)
        used[C[h]]+=1
        dfs(h)
        used[C[h]]-=1
dfs(0)
ans.append(1)
ans.sort()
print(*ans, sep='\n')