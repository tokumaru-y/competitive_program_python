W,H=list(map(int, input().split()))
N=int(input())
X1,X2,Y1,Y2=[],[],[],[]
def convert(list1, list2, limit):
    """座標圧縮
    """
    res1 = set()
    for element in list1:
        for i in range(-1, 2):
            d = element + i
            if 0<= d <= limit:res1.add(d)
    res2 = set()
    for element in list2:
        for i in range(-1, 2):
            d = element + i
            if 0<= d <= limit:res2.add(d)
    res1 = {v : i for i,v in enumerate(sorted(res1))}
    res2 = {v : i for i,v in enumerate(sorted(res2))}
    size = len(set(list(res1) + list(res2)))
    return res1, res2, size


for _ in range(N):
    x1,y1,x2,y2 = list(map(int, input().split()))
    X1.append(x1)
    Y1.append(y1)
    X2.append(x2)
    Y2.append(y2)

X1,X2,x_size = convert(X1, X2, W)
Y1,Y2,y_size = convert(Y1, Y2, H)
grid = [[0] * (x_size) for _ in range(y_size)]
for i in range(N):
    for h in range(Y1[i], Y2[i]+1):
        for w in range(X1[i], X2[i]+1):
            grid[h][w] = 1
ans = 0
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for h in range(y_size):
    for w in range(x_size):
        if grid[h][w]:continue
        grid[h][w]=1
        ans += 1
        q=deque()
        q.append([h,w])
        while len(q) > 0:
            nh,nw = q.popleft()
            for i in range(4):
                th = dx[i]
                tw = dy[i]
                if not (0<=th<=y_size and 0<=tw<=x_size):continue
                if grid[th][tw]:continue
                q.append([th,tw])
                grid[th][tw]=1
print(ans)