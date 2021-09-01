import sys
sys.setrecursionlimit(10**9)
N=int(input())
AB=[list(map(int, input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N)]
for a,b in AB:
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
for i in range(N):
    graph[i]=sorted(graph[i])
passed = [False]*N
ans = []
def search(top):
    passed[top] = True
    is_back = True
    for nt in graph[top]:
        if passed[nt]:continue
        if is_back:ans.append(top+1)
        is_back=False
        search(nt)
        ans.append(top+1)
    if is_back:ans.append(top+1)
search(0)
print(*ans)