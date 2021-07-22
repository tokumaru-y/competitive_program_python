N=int(input())
two = 0
four = 0
others = 0
A=list(map(int, input().split()))
for a in A:
    if a%4==0:
        four+=1
    elif a%2==0:
        two +=1
    else:
        others += 1
if others == 0:
    print("Yes")
else:
    if four >= others:
        print("Yes")
    elif four + others == N and four >= others - 1:
        print("Yes")
    else:
        print("No")
