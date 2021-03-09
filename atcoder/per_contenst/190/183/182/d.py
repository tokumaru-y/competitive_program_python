N=int(input())
A=list(map(int,input().split()))
max_num=float('-inf')
now_position=0
ans=0
sum=0
for a in A:
    max_num=max(max_num,sum+a) if max_num !=float('-inf') else a
    ans=max(ans,now_position+max_num)
    now_position+=a+sum
    sum+=a
print(ans)