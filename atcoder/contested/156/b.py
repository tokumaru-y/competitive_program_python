N,K=list(map(int,input().split()))
ans = []
while N != 0 :
    ans.append(N%K)
    N//=K
print(len(ans))