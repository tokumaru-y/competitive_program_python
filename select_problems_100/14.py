import copy
n,k=list(map(int,input().split()))
buildings=list(map(int,input().split()))

ans=float('inf')
for bit in range(1<<n):
    tmp_cnt=0
    tmp_k=0
    max_index=0
    max_high=buildings[0]
    tmp_builds=copy.deepcopy(buildings)
    for j in range(n):
        if bit & 1<<j:
            max_index=j
            tmp_k+=1
    if tmp_k < k:
        continue

    for j in range(1,max_index+1):
        if (bit & 1<<j):
            if max_high>=buildings[j]:
                tmp_cnt+=max_high+1 - buildings[j]
                max_high+=1
            else:
                max_high=max(max_high,buildings[j])
        else:
            max_high=max(max_high,buildings[j])
    ans=min(ans,tmp_cnt)
print(ans)