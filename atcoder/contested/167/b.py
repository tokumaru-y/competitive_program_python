l = list(map(int,input().split()))
ans = float('inf') 
if sum(l[:2]) >= l[3]:
    print(l[0] if l[0] <= l[3] else l[3])
else:
    print(l[0] - (l[3] - sum(l[:2])))