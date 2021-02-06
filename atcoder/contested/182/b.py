import math
n=int(input())
A = list(map(int,input().split()))
count_table={}
for a in A:
    for i in range(1,int(math.sqrt(a))+1):
        if a % i ==0:
            count_table.setdefault(i,0)
            count_table[i]+=1
            if a//i != i:
                count_table.setdefault(a//i,0)
                count_table[a//i]+=1
cnt = 0
del count_table[1]
for k,v in count_table.items():
    if cnt<v:
        cnt=v
        ans=k
print(ans)