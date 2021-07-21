a,b,c=list(map(int, input().split()))
x=2*b
y=a+c
ans = float("inf")
if x == y:
    ans = 0
elif x > y:
    ans = x-y
else:
    tmp = 0
    if y%2==1:
        tmp+=1
        y+=1
    ans = tmp+(y-x)//2
print(ans)