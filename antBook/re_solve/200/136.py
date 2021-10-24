# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_e
W,H=list(map(int, input().split()))
W*=2
H*=2
N=int(input())
X1,X2,Y1,Y2=[],[],[],[]
def convert(list1, list2, limit):
    """座標圧縮
    """
    res = set()
    for element in list1:
        for i in range(-1, 2):
            d = element + i
            if 0<= d <= limit:res.add(d)
    for element in list2:
        for i in range(-1, 2):
            d = element + i
            if 0<= d <= limit:res.add(d)
    res = {v : i for i,v in enumerate(sorted(res))}
    return res, len(res)

def format(list, format_list):
    res = []
    for elem in list:
        res.append(format_list[elem])
    return res
X1, X2, Y1, Y2 = [],[],[],[]
for _ in range(N):
    x1,y1,x2, y2 = list(map(int, input().split()))
    X1.append(x1*2)
    X2.append(x2*2)
    Y1.append(y1*2)
    Y2.append(y2*2)
conv_x, size_x = convert(X1, X2, W)
conv_y, size_y = convert(Y1, Y2, H)
X1 = format(X1, conv_x)
X2 = format(X2, conv_x)
Y1 = format(Y1, conv_y)
Y2 = format(Y2, conv_y)
grid = [[0] * (size_x) for _ in range(size_y)]
for i in range(N):
    for h in range(Y1[i], Y2[i]+1):
        for w in range(X1[i], X2[i]+1):
            grid[h][w] = 1
ans = 0
dx = [0,1,-1,0]
dy = [1,0,0,-1]
from collections import deque
for h in range(size_y):
    for w in range(size_x):
        if grid[h][w]:continue
        ans += 1
        q = deque()
        q.append([h,w])
        grid[h][w]=1
        while len(q)>0:
            nh,nw = q.popleft()
            for i in range(4):
                th,tw = dx[i]+nh, dy[i]+nw
                if not(0<=th<size_y and 0<=tw<size_x):continue
                if grid[th][tw]:continue
                grid[th][tw]=1
                q.append([th,tw])
print(ans)