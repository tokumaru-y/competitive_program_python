import math
n=int(input())
abs_list=[]
yugrid=[]
in_list=list(map(int,input().split()))
for i in in_list:
    abs_list.append(abs(i))
    yugrid.append(i**2)
a=sum(abs_list)
b=sum(yugrid)
c=max(abs_list)
print(a)
print(math.sqrt(b))
print(c)