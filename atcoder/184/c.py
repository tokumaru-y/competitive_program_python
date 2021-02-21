a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))
p=abs(c-a)
q=abs(b-d)
if p==0 and q==0:
    print(0)
elif p==q or p+q<=3:
    print(1)
elif (p+q)%2==0 or p+q<=6 or abs(p-q) <= 3:
    print(2)
else:
    print(3)

