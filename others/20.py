import math
N=int(input())
A=list(map(int, input().split()))
table_a={}
for a in A:
    for i in range(2, math.isqrt(a)+1):
        if a%i==0:
            if i not in table_a:table_a[i]=0
            while a%i==0:
                table_a[i]+= 1
                a//=i
    if a!=1:
        if a not in table_a:
            table_a[a]=1
        else:
            table_a[a]+=1
M=int(input())
B=list(map(int, input().split()))
table_b={}
for b in B:
    for i in range(2, math.isqrt(b)+1):
        if b%i==0:
            if i not in table_b:table_b[i]=0
            while b%i==0:
                table_b[i]+=1
                b//=i
    if b!=1:
        if b not in table_b:
            table_b[b] = 1
        else:
            table_b[b]+=1
if table_a == table_b:
    print("Yes")
else:
    print("No")
