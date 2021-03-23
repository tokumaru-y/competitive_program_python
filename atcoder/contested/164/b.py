a,b,c,d = list(map(int,input().split()))
for i in range(205):
    if i%2==0:
        c -= b
    else:
        a -=d
    if a<=0:
        print("No")
        exit()
    elif c<=0:
        print("Yes")
        exit()