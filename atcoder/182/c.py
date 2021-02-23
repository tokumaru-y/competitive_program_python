N=list(input().rstrip())
N.reverse()
ln=len(N)
ans=float('inf')
for b in range(1,1<<ln):
    used=0
    t=0
    for i in range(ln):
        if b & 1<<i:
            t+=int(N[i])*10**used
            used+=1
    if t%3==0:
        ans = min(ans,ln - used)
print(ans if ans!=float('inf') else -1)