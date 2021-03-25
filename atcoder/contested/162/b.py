N=int(input())
al = N*(1+N)//2
for i in range(1,N+1):
    if i%3==0 or i%5==0:
        al -= i
print(al)