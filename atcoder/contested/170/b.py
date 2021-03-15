X,Y=list(map(int,input().split()))
for i in range(X+1):
    turu = i * 2
    kame = (X-i)*4
    if turu+kame == Y:
        print("Yes")
        exit()
print("No")