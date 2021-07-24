import sys
sys.setrecursionlimit(10**9)
from heapq import heapify,heappop,heappush
N,M=list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b=list(map(int, input().split()))
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
# 距離,頂点
h = [[0, 0]]
ans = 0
distance = [float("inf")] * N
distance[0]=0
passed_cnt = [0] * N
passed_cnt[0]=1
MOD = 10**9+7
heapify(h)
while len(h)>0:
    d,t = heappop(h)
    for nt in graph[t]:
        if distance[nt]<d+1:continue
        passed_cnt[nt]+=passed_cnt[t]
        passed_cnt[nt]%=MOD
        if distance[nt] == d+1:continue
        distance[nt]=d+1
        # if nt == N-1:
        #     print("aaaa")
        #     print(nt,t)
        #     ans += passed_cnt[t]
        #     ans %= MOD
        #     continue
        if nt != N-1:heappush(h, [d+1, nt])
# print(passed_cnt)
# print(distance)
if distance[N-1]==float("inf"):
    print(0)
    exit()
print(passed_cnt[N-1])
# h=[[0,0]]
# heapify(h)
# print(passed_cnt)
# print(distance)
# ans =1
# def dfs(top, cost):
#     global ans
#     for nt in graph[top]:
#         if distance[nt] == cost+1:
#             ans *= passed_cnt[nt]
#             ans %= MOD
#             dfs(top,cost+1)
# dfs(0,0)
# # while len(h)>0:
# #     d,t = heappop(h)
# #     for nt in graph[t]:
# #         if distance[nt]==d+1:
# #             ans *= passed_cnt[nt]
# #             ans %= MOD
# #             print(t,nt, ans)
# #             heappush(h,[distance[nt],nt])
