N=int(input())
tmp=0
for _ in range(N):
    a,b=list(map(int,input().split()))
    if a==b:
        tmp+=1
    else:
        tmp=0
    if tmp>=3:
        print("Yes")
        exit()
print("No")