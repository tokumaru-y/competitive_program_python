n,m=list(map(int,input().split()))
switches=[list(map(int,input().split()[1:])) for _ in range(m)]
p_list=list(map(int,input().split()))

ans=0
for bit in range((1<<n)):
    flag=True
    for j in range(m):
        tmp_cnt=0
        for k in switches[j]:
            if bit & (1<<k-1):
                tmp_cnt+=1
        if tmp_cnt % 2 != p_list[j]:
            flag=False
            continue
    if flag:
        ans+=1
print(ans)
