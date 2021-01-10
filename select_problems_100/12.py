n,m=list(map(int,input().split()))
relations=[[False]*(n+1) for _ in range(n)]
for _ in range(m):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    relations[a][b]=True
    relations[b][a]=True
ans=0
for bit in range(1<<n):
    tmp_members=[]
    for j in range(n):
        if bit&(1<<j):
            tmp_members.append(j)
    flag=True
    for t in tmp_members:
        for t_i in tmp_members:
            if t==t_i:
                continue
            if not relations[t][t_i]:
                flag=False
    ans=max(ans,len(tmp_members)) if flag else ans
print(ans)