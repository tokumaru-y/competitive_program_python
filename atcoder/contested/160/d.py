from collections import deque
N,X,Y = list(map(int, input().split()))
X,Y = X-1, Y-1
node = [[] for _ in range(N)]
for i in range(N-1):
    node[i].append(i+1)
    node[i+1].append(i)
    if i==X:
        node[X].append(Y)
        node[Y].append(X)
leng = []
def BFS(x):
    q = deque([x])
    tmp = [0]*N
    passed = [False]*N
    passed[x] = True
    while len(q)>0:
        next = q.popleft()
        for n in node[next]:
            if passed[n]:continue
            tmp[n] = tmp[next]+1
            passed[n] = True
            q.append(n)
    return tmp

cost = [BFS(i) for i in range(N)]
for k in range(1, N):
    ans = 0
    for c in cost:
        ans += c.count(k)
    print(ans//2)