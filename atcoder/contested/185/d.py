import copy
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
gcdlist=copy.deepcopy(a)
gcdlist.append(0)
gcdlist.append(n)
gcdlist=list(set(gcdlist))
gcdlist.sort()
a.sort()
span = float('inf')
ans=0
for i in range(1,len(gcdlist)):
    if gcdlist[i]==1 or gcdlist[i]-1==gcdlist[i-1]:continue
    span=min(span,gcdlist[i]-1-gcdlist[i-1])
pre = 0
if span == 0 or n==m:
    print(0)
    exit(0)
elif m==0:
    print(1)
    exit(0)
for i in a:
    if i == 1:
        pre = i
        continue
    if pre!=1:
        ans += ()
    else:
        ans+= (i-1-pre)//span if  (i-1-pre)%span==0 else (i-1-pre)//span + 1
    pre = i
if n!=pre:
    ans += (n-pre)//span if (n-pre)%span==0 else (n-pre)//span + 1
print((ans))

now doing...