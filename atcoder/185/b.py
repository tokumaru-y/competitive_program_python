import sys
n,m,t=list(map(int,input().split()))
time_table=[list(map(int,input().split())) for _ in range(m)]
bateries=n
pre=0
for a,b in time_table:
    bateries-=(a-pre)
    pre=b
    if bateries<=0:
        print("No")
        exit(0)
    bateries+=(b-a)
    bateries=min(bateries,n)
bateries-=t-pre
if bateries<=0:
    print("No")
else:
    print("Yes")