## TODO https://atcoder.jp/contests/tdpc/tasks/tdpc_tree
MAX = 10**6+5
MOD=10**9+7
fac=[0] * MAX
finv=[0]* MAX
inv=[0] * MAX
# テーブルの初期化
def COMinit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

COMinit()
N=int(input())
MOD=10**9+7
dp=[[0] * N for _ in range(N)]
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
    own_size = 0
    dp[v] = [0] * element_count_by[v]
    for ind in range(element_count_by[v]):
        next_v = graph[v][ind]
        if next_v == parent:
            parent_element[v] = ind
            continue
        size, tmp_res = dfs(next_v, v)
        res *= (tmp_res)
        res %= MOD
        own_size+=size+1
        dp[v][ind]=tmp_res%MOD
    res *= fac[own_size]
    res %= MOD
    return own_size, res

def bfs(v, res_parent_value=-1, parent=-1):
    if parent != -1:
        dp[v][parent_element[v]] = res_parent_value
    dpl = [1]*(element_count_by[v]+1)
    for i in range(element_count_by[v]):
        dpl[i+1]=dpl[i]*(dp[v][i]+1)%MOD
    dpr = [1]*(element_count_by[v]+1)
    for i in range(element_count_by[v]-1, -1, -1):
        dpr[i] = dpr[i+1]*(dp[v][i]+1)%MOD
    ans[v]=dpr[0]
    for i in range(element_count_by[v]):
        next_v = graph[v][i]
        if next_v == parent:continue
        bfs(next_v, dpl[i] * dpr[i+1]%MOD, v)

dfs(0)
print(dp)
bfs(0)
print(dp)
print(ans)