N,K=list(map(int,input().split()))
t=str(N)
for _ in range(K):
    t1=sorted(t, reverse=True)
    t2=sorted(t)
    t=str(int(''.join(t1)) - int(''.join(t2)))
print(t)