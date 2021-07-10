MAX = 1000000+1
prime_list = [True]*MAX
is_minus_count = [0]*MAX
prime_list[0]=False
prime_list[1]=False
for i in range(2,MAX):
    is_minus_count[i]+=is_minus_count[i-1]
    if not prime_list[i]:continue
    k=i+i
    cnt = 1
    while k<MAX:
        prime_list[k]=False
        is_minus_count[k]+=cnt
        k+=i
        cnt+=1
t=int(input())
for _ in range(t):
    try:
        n=int(input())
        total = (n)*(n-1)//2 + 2
        print(total-is_minus_count[n])
    except:
        break
#TODO わからん