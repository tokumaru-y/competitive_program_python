from collections import deque
N,M=list(map(int, input().split()))
cnt = [[] for _ in range(N)]
boals = []
next_q = deque()
remove_cnt = 0
for i in range(M):
    K=int(input())
    tmp = deque()
    inp = list(map(int, input().split()))
    for k in range(K):
        tmp.append(inp[k]-1)
    cnt[tmp[0]].append(i)
    if len(cnt[tmp[0]]) == 2:
        next_q.append(tmp[0])
        remove_cnt += 1
    boals.append(tmp)
while len(next_q) > 0:
    next_color = next_q.popleft()
    for nt in cnt[next_color]:
        boals[nt].popleft()
        if len(boals[nt]) == 0:continue
        target = boals[nt][0]
        cnt[target].append(nt)
        if len(cnt[target]) == 2:
            next_q.append(target)
            remove_cnt+=1
if remove_cnt == N:
    print("Yes")
else:
    print("No")