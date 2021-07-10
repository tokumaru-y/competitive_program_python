import bisect
import sys
input = sys.stdin.readline
N,M=list(map(int, input().split()))
P=[]
for _ in range(N):
    P.append(int(input()))
P.append(0)
sump=[]
for i in range(len(P)):
    for j in range(i,len(P)):
        sump.append(P[i]+P[j])
sump.sort()

ans = float('-inf')
for i in range(len(sump)):
    left = M - sump[i]
    if left<0:break
    ind = bisect.bisect_right(sump,left)
    ind -= 1
    if sump[i] + sump[ind] > M:continue
    ans = max(ans, sump[i]+sump[ind])
print(ans if ans != float('-inf') else 0)