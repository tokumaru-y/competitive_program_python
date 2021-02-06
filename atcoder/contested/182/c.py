n=input().rstrip()
ans=float('inf')
ll = len(n)
for bit in range(1<<ll):
    tmp_cnt=0
    tmp_sum=0
    for i in range(ll):
        if bit & 1<<i:
            tmp_sum+=int(n[i])
            tmp_cnt+=1
    if tmp_sum % 3==0:
        ans=min(ans,ll-tmp_cnt)
print(ans if ans != ll else -1)