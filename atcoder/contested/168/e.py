import math
N=int(input())
AB=[list(map(int,input().split())) for _ in range(N)]
MOD = 10**9
tilt_list = {}
zero_cnt = 0
for ind, a, b in enumerate(AB):
    if a==0 or b==0:
        a = 1 if a!=0 else 0
        b = 1 if b!=0 else 0
    is_exist = True if [a,b] in tilt_list else False
    if a==0 and b==0:
        zero_cnt+=1
        continue
    elif a==0 or b==0:
        if is_exist:
            tilt_list[[a,b]] +=1
        else:
            tilt_list[[a,b]] =1
    gcd = math.gcd(a,b)
    if b < 0:
        a = (a//gcd) * -1
        b = (b//gcd) * -1
        if is_exist:
            tilt_list[[a,b]] +=1
        else:
            tilt_list[[a,b]] =1    
    else:
        if is_exist:
            tilt_list[[a,b]] +=1
        else:
            tilt_list[[a,b]] =1

all_cnt = (2**(N-zero_cnt))-1
all_cnt %= MOD
for k,v in tilt_list.items():
    tmp_cnt = 0
    a,b = k
    if a == 0 or b == 0:
        sa = 0 if a==0 else 1
        sb = 0 if b==0 else 1
        all_cnt -= 