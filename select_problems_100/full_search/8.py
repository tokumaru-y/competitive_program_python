import sys
import math
sys.setrecursionlimit(10**9)
n=int(sys.stdin.readline().rstrip())
goods=[]
for _ in range(n):
    goods.append(list(map(int,sys.stdin.readline().rstrip().split())))
ans=float('inf')
for start in range(n):
    for end in range(n):
        dis1=goods[start][0]
        dis2=goods[end][1]
        tmp = 0
        for i in range(n):
            s,e=goods[i]
            tmp+=min(
                abs(dis1-s)+abs(s-e)+abs(dis2-e),
                abs(dis1-e)+abs(s-e)+abs(dis2-s)
            )
        else:
            ans = min(ans,tmp)
print(ans)