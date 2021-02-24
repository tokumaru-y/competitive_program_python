X,Y,A,B=list(map(int,input().split()))
ans=0
for i in range(105):
    p=A**i
    if (X*p)>=Y:
        break
    d = (Y-X*p)//B
    if X*p+d*B>=Y:d-=1
    ans = max(ans, i+d)
print(ans)
