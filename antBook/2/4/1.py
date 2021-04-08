import itertools
from collections import deque
N,M=list(map(int, input().split()))
roads = [[] for _ in range(N)]
for _ in range(M):
    a,b=list(map(lambda x : int(x)-1, input().split()))
    roads[a].append(b)
    roads[b].append(a)
target_list = [i for i in range(N)]
ans = 0
for ll in itertools.permutations(target_list):
    if ll[0] != 0:continue
    flag = True
    for i in range(N-1):
        if ll[i+1] not in roads[ll[i]]:flag = False
    if flag:ans+=1
print(ans)