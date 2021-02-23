N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            a,b=XY[i]
            c,d=XY[j]
            x,y=XY[k]
            if (a-x)*(b-d) == (b-y)*(a-c):
                print("Yes")
                exit()
print("No")