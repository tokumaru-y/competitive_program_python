N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
min_num=A[-1]
ans = A[0]
cnt = {}
for a in A[1:]:
    if a in cnt:
        cnt[a]+=1
    else:
        cnt[a]=1
for k,v in cnt.items():
    if k==min_num:
        ans+=k*(v-1)
    else:
        ans+=k*v
print(ans)