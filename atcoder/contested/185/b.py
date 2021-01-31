n,m,t=list(map(int,input().split()))
batteries=n
roots=[False]*t
for _ in range(m):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    for i in range(a+1,b+1):
        roots[i] = True
for i in range(t):
    if roots[i]:
        batteries = min(n,batteries+1)
    else:
        batteries -= 1
    if batteries <= 0:
        print("No")
        exit(0)
print("Yes")