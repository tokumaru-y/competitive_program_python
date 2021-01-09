import sys
n=int(input())
in_list=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    a,b = in_list[i]
    for j in range(i+1,n):
        x,y = in_list[j]
        if x==a:
            continue
        dif=(y-b)/(x-a)
        if -1 <= dif <= 1:
            ans+=1
print(ans)