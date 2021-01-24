n=int(input())
ll=list(map(int,input().split()))
ans=0
for i in range(n):
    target=ll[i]
    tmp_cnt=0
    for j in range(n):
        if target<=ll[j]:
            tmp_cnt+=target
        else:
            ans=max(ans,tmp_cnt)
            tmp_cnt=0
    ans=max(ans,tmp_cnt)
print(ans)