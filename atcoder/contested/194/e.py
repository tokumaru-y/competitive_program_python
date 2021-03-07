N,M=list(map(int,input().split()))
A=list(map(int,input().split())) 
count = {}
ans=N
for i in range(M):
    if A[i] in count:
        count[A[i]] += 1
    else:
        count[A[i]] = 1
for i in range(N):
   if not i in count:
       ans = i
       break
for i in range(N-M):
    count[A[i]]-=1
    if not A[i+M] in count:
        count[A[i+M]]=1
    else:
        count[A[i+M]]+=1
    if count[A[i]]==0:
        ans=min(ans, A[i])
print(ans)