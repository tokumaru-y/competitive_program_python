n=int(input())
ll=list(map(int,input().split()))

prime_number=[True]*1001
prime_number[0]=False
prime_number[1]=False
prime_list=[]
for i in range(2,1001):
    if not prime_number[i]:
        continue
    else:
        prime_list.append(i)
        tmp=2
        while i*tmp<=1000:
            prime_number[i*tmp]=False
            tmp+=1

ans=0
cnt=0
for p in prime_list:
    tmp_cnt=0
    for l in ll:
        tmp_cnt += 1 if l % p == 0 else 0
    else:
        if tmp_cnt>cnt:
            cnt=tmp_cnt
            ans=p
print(ans)