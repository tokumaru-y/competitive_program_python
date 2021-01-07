from itertools import combinations
N = int(input())
ls = []
for n in range(N):
    x,y = map(int,input().split())
    ls.append((x,y))

ls.sort()
st = set(ls)
ans=0
for p1,p2 in combinations(ls,2):
    x1,y1 = p1
    x2,y2 = p2
    if (x2+y2-y1,y2+x1-x2) in st and (x1+y2-y1,y1+x1-x2) in st:
        ans = max(ans,(x1-x2)**2+(y1-y2)**2)
print(ans)