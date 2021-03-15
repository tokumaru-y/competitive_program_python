X,N=list(map(int,input().split()))
num = [True] * 202
P=list(map(int,input().split()))
for p in P:
    p+=100
    num[p]=False

for i in range(102):
    ans1= X-i
    ans2= X+i
    if num[ans1+100]:
        print(ans1)
        exit()
    if num[ans2+100]:
        print(ans2)
        exit()
