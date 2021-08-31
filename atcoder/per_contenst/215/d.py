from math import sqrt
N,M=list(map(int, input().split()))
A=list(map(int, input().split()))
prime_list = [True] * (M+1)
prime_list[0]=False
prime_list[1]=False
num_list = []
for a in A:
    if a == 1:continue
    for i in range(1, int(sqrt(a))+1):
        if i == 1:
            k = a
            if k> M or not prime_list[k]:continue
            while k<=M:
                prime_list[k]=False
                k+=a
        elif a%i==0:
            x,y = i,a//i
            for k in [x,y]:
                if k>M or not prime_list[k]:continue
                t=k
                while t<=M:
                    prime_list[t]=False
                    t+=k
ans_cnt = 1
ans_list = [1]
for i in range(2,M+1):
    if prime_list[i]:
        ans_cnt+=1
        ans_list.append(i)
print(ans_cnt)
print(*ans_list, sep="\n")