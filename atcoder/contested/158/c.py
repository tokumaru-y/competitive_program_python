import math
A,B=list(map(int, input().split()))
for i in range(1,1010):
    a = math.floor(i*8/100)
    b = math.floor(i*10/100)
    if a==A and b==B:
        print(i)
        exit()
print(-1)