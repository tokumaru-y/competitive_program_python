from collections import deque
from sys import path
N,M=list(map(int,input().split()))
AB=[list(map(int,input().split())) for _ in range(M)]
path_list = [[] for _ in range(N)]
for a,b in AB:
    a,b=a-1,b-1
    path_list[a].append(b)
    path_list[b].append(a)
ans = [-1] * (N)
ans[0] = "Yes"
paths = deque([1])
while len(paths) > 0:
    next = paths.popleft()
    for n in path_list[next-1]:
        if ans[n] != -1:continue
        ans[n]=next
        paths.append(n+1)
if ans.count(-1) > 0:
    print("No")
else:
    print(*ans, sep='\n')