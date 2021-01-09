n,x=list(map(int,input().split()))
s=input().rstrip()
ans=x
for c in s:
    if c=='x':
        ans -= 1
    else:
        ans+=1
    ans = ans if ans>=0 else 0
print(ans)