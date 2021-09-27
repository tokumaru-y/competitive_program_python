K=int(input())
A,B=input().split()
Ax=0
for idx, a in enumerate(list(reversed(A))):
    Ax += int(a) * K**(idx)
Bx=0
for idx, b in enumerate(list(reversed(B))):
    Bx += int(b) * K**(idx)
print(Ax*Bx)