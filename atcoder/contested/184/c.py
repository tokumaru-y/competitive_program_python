x,y=list(map(int,input().split()))
a,b=list(map(int,input().split()))
p=abs(a-x)
q=abs(b-y)
if p == 0 and q ==0:
    print(0)
elif p==q or p+q<=3:
    print(1)
elif (p+q)%2==0 or p+q <=6 or abs(p-q) <=3:
    print(2)
else:
    print(3)