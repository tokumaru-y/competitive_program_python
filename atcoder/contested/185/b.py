n,m,t=list(map(int,input().split()))
batteries=n
pre = 0
for i in range(m):
    a,b=list(map(int,input().split()))
    batteries-=a - pre
    if batteries <= 0:
        print("No")
        exit(0)
    pre = b
    batteries=min(b-a+batteries,n)
print("Yes" if (t-pre) < batteries else "No")