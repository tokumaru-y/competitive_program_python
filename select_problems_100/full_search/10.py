n=int(input())
n_list=list(map(int,input().split()))
q=int(input())
q_list=list(map(int,input().split()))
hash_table={}
for i in range(1<<n):
    tmp_cnt=0
    for j in range(n):
        if i & 1<<j:
            tmp_cnt+=n_list[j]
    hash_table[tmp_cnt]=1
for ql in q_list:
    if hash_table.get(ql):
        print("yes")
    else:
        print("no")