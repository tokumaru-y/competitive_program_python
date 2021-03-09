N,M=list(map(int,input().split()))
if M==0:
    print(1)
    exit()
A=list(map(int,input().split()))
if A[-1]!=N:A.append(N+1)
spans=[]
pre=0
mnum=float('inf')
A.sort()
for a in A:
    if a == pre+1:
        pre=a
        continue
    spans.append(a-pre-1)
    mnum=min(mnum,a-pre-1)
    pre = a
if len(A) == N:
    print(0)
else:
    ans=0
    for s in spans:
        ans += s//mnum
        if s%mnum!=0:ans+=1
    print(ans)