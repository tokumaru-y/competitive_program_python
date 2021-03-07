N,X=list(map(int,input().split()))
sum_al=0
for i in range(N):
    v,p=list(map(int,input().split()))
    sum_al += v*p
    if sum_al > X *100:
        print(i+1)
        exit()
print(-1)