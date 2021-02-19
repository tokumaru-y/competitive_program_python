N,M,T=list(map(int,input().split()))
events=[]
pre=0
for _ in range(M):
    a,b=list(map(int,input().split()))
    events.append(pre-a)
    events.append(b-a)
    pre=b
events.append(pre-T)
battery = N
for t in events:
    battery=min(N,battery+t)
    if battery<=0:
        print("No")
        exit()
print("Yes")