N,W=list(map(int,input().split()))
accumulations=[0]*(2*10**5+10)
for _ in range(N):
    s,t,p=list(map(int,input().split()))
    accumulations[s]+=p
    accumulations[t]-=p
for i in range(2*10**5+10):
    accumulations[i]+=accumulations[i-1] if i >0 else 0
    if accumulations[i]>W:
        print("No")
        exit()
print("Yes")