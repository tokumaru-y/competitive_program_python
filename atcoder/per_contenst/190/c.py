N,M=list(map(int,input().split()))
AB=[]
for _ in range(M):
    a,b=list(map(int,input().split()))
    a,b=a-1,b-1
    AB.append([a,b])
K=int(input())
CD=[]
for _ in range(K):
    c,d=list(map(int,input().split()))
    c,d=c-1,d-1
    CD.append([c,d])
ans=0
for bit in range(1<<K):
    tmp=[False]*N
    tmp_cnt=0
    for j in range(K):
        if bit & 1<<j:
            tmp[CD[j][0]]=True
        else:
            tmp[CD[j][1]]=True
    for i in range(M):
        if tmp[AB[i][0]] and tmp[AB[i][1]]:
            tmp_cnt+=1
    ans=max(ans,tmp_cnt)
print(ans)