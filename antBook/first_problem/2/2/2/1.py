N=int(input())
d = []
for i in range(N):
    x,l=list(map(int, input().split()))
    s=x-l
    e=x+l
    d.append([e,s])
d.sort()
limit = float('-inf')
leave = 0
for i in range(N):
    e,s=d[i]
    if s >= limit:
        limit = e
    else:
        leave+=1
print(N-leave)
