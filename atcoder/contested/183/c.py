import itertools
n,k=list(map(int,input().split()))
time_table=[list(map(int,input().split())) for _ in range(n)]
cities = [i+1 for i in range(n-1)]
ans=0
for per_list in itertools.permutations(cities):
    tmp_sum=0
    pre = 0
    for c in per_list:
        tmp_sum+=time_table[pre][c]
        pre=c
    tmp_sum+=time_table[pre][0]
    if tmp_sum == k:
        ans+=1
print(ans)