N,X=list(map(int,input().split()))
ans=[]
ll=list(map(int,input().split()))
for l in ll:
    if l==X:continue
    ans.append(l)
print(*ans)