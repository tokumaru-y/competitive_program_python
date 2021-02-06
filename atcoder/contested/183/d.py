n,w=list(map(int,input().split()))
table=[list(map(int,input().split())) for _ in range(n)]
sort_table=sorted(table,key=lambda x : x[1])
time_table=[0]*(2*10**5+10)
for s,t,p in sort_table:
    time_table[s]+=p
    time_table[t]-=p
for i in range(2*10**5+1):
    time_table[i]+=time_table[i-1] if i != 0 else 0
    if time_table[i]>w:
        print("No")
        exit(0)

print("Yes")