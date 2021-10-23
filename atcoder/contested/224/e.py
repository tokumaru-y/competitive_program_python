import sys
input = sys.stdin.readline
H,W,N=list(map(int, input().split()))
RCA = [list(map(int, input().split())) for _ in range(N)]
tmp_set_r = []
tmp_set_c = []
for r,c,a in RCA:
    tmp_set_r.append(r)
    tmp_set_c.append(c)
comp_r = {x:i for i,x in enumerate(list(sorted(list(set(tmp_set_r)))))}
comp_c = {x:i for i,x in enumerate(list(sorted(list(set(tmp_set_c)))))}
graph_r = [[] for _ in range(len(comp_r))]
graph_c = [[] for _ in range(len(comp_c))]
 
for i in range(N):
    r,c,a = RCA[i]
    _r = comp_r[r]
    _c = comp_c[c]
    graph_r[_r].append(i)
    graph_c[_c].append(i)
sys.setrecursionlimit(10**9)
# deapth = [-1] * N
cnt = [-1] * N
def dfs(i,r,c,a,d):
    res = d
    if cnt[i] >= 0:return cnt[i]
    # deapth[i]=d
    tmp_set = list(set(graph_c[c] + graph_r[r]))
    for _idx in tmp_set:
        _r,_c,_a = RCA[_idx]
        if a >= _a:continue
        res = max(res, dfs(_idx,comp_r[_r], comp_c[_c], _a, d+1))
    cnt[i] = res
    return res
    # for _idx in graph_r[r]:
    #     _r,_c,_a = RCA[_idx]
    #     if a >= _a or deapth[_idx] >=0:continue
    #     res = max(res, dfs(_idx,comp_r[_r], comp_c[_c], _a, d+1))
    # for _idx in graph_c[c]:
    #     _r,_c,_a = RCA[_idx]
    #     if a >= _a or deapth[_idx] >= 0:continue
    #     res = max(res, dfs(_idx,comp_r[_r], comp_c[_c], _a, d+1))
 
    return res
for i in range(N):
    r,c,a = RCA[i]
    r=comp_r[r]
    c=comp_c[c]
    if cnt[i] >= 0:
        print(cnt[i])
    else:
        print(dfs(i,r,c,a,0))