n,c=list(map(int,input().split()))
events=[]
for _ in range(n):
    a,b,co=list(map(int,input().split()))
    events.append((a-1,co))
    events.append((b,-co))
events.sort()
ans=0
now=0
charges=0
for day,cost in events:
    if now != day:
        ans+=min(c,charges) * (day-now)
        now=day
    charges+=cost
print(ans)