n,m=list(map(int,input().split()))
target=[list(map(int,input().split())) for _ in range(m)]

k=int(input())
how=[]
for _ in range(k):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    how.append([a,b])
ans=0
for bit in range(1<<k):
    inlist=[False]*n
    for j in range(k):
        tm = how[j]
        if bit & 1<<j:
            inlist[tm[1]]=True
        else:
            inlist[tm[0]]=True
    tmp_cnt=0
    for a,b in target:
        a-=1
        b-=1
        if inlist[a] and inlist[b]:
            tmp_cnt+=1
    ans=max(ans,tmp_cnt)
print(ans)