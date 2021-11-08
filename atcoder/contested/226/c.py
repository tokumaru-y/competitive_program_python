from collections import deque


N=int(input())
cost = [0] * N
need = [[] for _ in range(N)]
for i in range(N):
    inl = list(map(int, input().split()))
    cost[i] = inl[0]
    if inl[1] > 0:
        need[i] += inl[2:]
q = deque([N-1])
ans = 0
passed = [False] * N
passed[N-1] = True
while len(q) > 0:
    v = q.popleft()
    ans += cost[v]
    for nv in need[v]:
        if passed[nv-1]:continue
        passed[nv-1] = True
        q.append(nv-1)
print(ans)