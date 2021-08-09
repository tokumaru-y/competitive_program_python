## TODO https://atcoder.jp/contests/tdpc/tasks/tdpc_tree

N=int(input())
MOD=10**9+7
dp=[[0] for _ in range(N)]
ans=[0]*N
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
ans = [0] * N
element_count_by = [0] * N
parent_element = [0] * N
def dfs(v,parent=-1):
    element_count_by[v]=len(graph[v])
    res = 1
    for ind in range(element_count_by[v]):
        if graph[v][ind] == parent:
            parent_element[v] = ind
            continue
        dp[v][ind] = dfs(graph[v][ind], v)
        res += dp[v][ind]
        dp[v][ind] %= MOD

def bfs(v, res_parent_value=-1, parent=-1):
    pass

dfs(0)
bfs(0)