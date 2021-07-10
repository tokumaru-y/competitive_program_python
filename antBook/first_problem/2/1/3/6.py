from collections import deque
import sys
input = sys.stdin.readline
while True:
    N,M=list(map(int, input().split()))
    if N+M == 0:break
    _, *a = list(map(int, input().split()))
    _, *b = list(map(int, input().split()))
    _, *c = list(map(int, input().split()))
    a.insert(0,0)
    b.insert(0,0)
    c.insert(0,0)
    d = deque([])
    d.append([a,b,c,0,-1])
    target = [i for i in range(N+1)]
    while len(d) > 0:
        a,b,c,cnt,pre = d.popleft()
        if cnt > M:
            print(-1)
            break
        if a== target or c ==target:
            print(cnt)
            break
        if a[-1] > b[-1] and pre != 2:
            d.append([a[:-1], b+[a[-1]], c, cnt+1, 1])
        if b[-1] > a[-1] and pre != 1:
            d.append([a+[b[-1]], b[:-1], c, cnt+1, 2])
        if b[-1] > c[-1] and pre != 4:
            d.append([a, b[:-1], c+[b[-1]], cnt+1, 3])
        if c[-1] > b[-1] and pre != 3:
            d.append([a,b+[c[-1]],c[:-1], cnt+1, 4])

