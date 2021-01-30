n,s,d=list(map(int,input().split()))
for _ in range(n):
    x,y=list(map(int,input().split()))
    if x < s and y > d:
        print("Yes")
        exit(0)
print("No")