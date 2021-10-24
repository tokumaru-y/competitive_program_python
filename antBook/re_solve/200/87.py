N,M,S,T=list(map(int,input().split()))
S-=1
T-=1
moneies = [[] for _ in range(N)]
snuukes = [[] for _ in range(N)]
for i in range(M):
    u,v,a,b = list(map(int, input().split()))
    u-=1
    v-=1
    moneies[u].append([v,a])
    moneies[v].append([u,a])
    snuukes[u].append([v,b])
    snuukes[v].append([u,b])
money_costs = [float("inf")] * N
snuuke_costs = [float("inf")] * N
money_costs[S]=0
snuuke_costs[T]=0
from heapq import heapify, heappop,heappush
def fix_costs(is_money,s):
    h = [[0,s]]
    heapify(h)
    if is_money:
        graph = moneies
        cost_table = money_costs
    else:
        graph = snuukes
        cost_table = snuuke_costs
    while len(h) > 0:
        oc,ot = heappop(h)
        for nt,tc in graph[ot]:
            nc = oc + tc
            if cost_table[nt] <= nc:continue
            cost_table[nt] = nc
            heappush(h,[nc, nt])
    return cost_table
money_costs = fix_costs(True,S)
snuuke_costs = fix_costs(False,T)
ans = []
now_num = float("inf")
for i in reversed(range(N)):
    now_num = min(now_num, money_costs[i] + snuuke_costs[i])
    ans.append(10**15-now_num)
ans.reverse()
print(*ans, sep="\n")