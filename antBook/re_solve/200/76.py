from collections import defaultdict
d = defaultdict(int)
N=int(input())
for _ in range(N):
    a=input()
    if a in d:
        d[a]+=1
    else:
        d[a]=1
M=int(input())
for _ in range(M):
    a=input()
    if a in d:
        d[a]-=1
    else:
        d[a]=-1
print(max(list(d.values()) + [0]))