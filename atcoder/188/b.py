n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum_num=0
for i,j in zip(a,b):
    sum_num+=i*j
if sum_num == 0:
    print("Yes")
else:
    print("No")