n,x=list(map(int,input().split()))
tmp=0
for i in range(n):
    a,b=list(map(int,input().split()))
    tmp+=a*b
    if tmp > x*100:
        print(i+1)
        exit(0)

print(-1)