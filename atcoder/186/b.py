h,w=list(map(int,input().split()))
min_num = float('inf')
sum_blocks= 0
for _ in range(h):
    in_list=list(map(int,input().split()))
    min_num=min(min_num,min(in_list))
    sum_blocks+=sum(in_list)
ans=max(sum_blocks - (h*w)*min_num,0)
print(ans)