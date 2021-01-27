n=int(input())
seven_cnt=0
for i in range(1,n+1):
    s_num=str(i)
    s_e_num=str(oct(i))
    if '7' in s_num or '7' in s_e_num:
        seven_cnt+=1
print(n-seven_cnt)