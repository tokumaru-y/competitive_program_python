n=int(input())
dif=0
in_list=[]
for _ in range(n):
    a,b=list(map(int,input().split()))
    dif-=a
    in_list.append(a+a+b)
in_list.sort(reverse=True)
for i in range(n):
    dif+=in_list[i]
    if dif > 0:
        print(i+1)
        exit(0)
