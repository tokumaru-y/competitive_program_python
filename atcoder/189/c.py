N=int(input())
A=list(map(int,input().split()))
ans=0
for i in range(N):
    min_num=A[i]
    tmp_sum=0
    for j in range(N):
        if min_num > A[j]:
            ans=max(ans,tmp_sum)
            tmp_sum=0
        else:
            tmp_sum+=min_num
    ans=max(ans,tmp_sum)
print(ans)