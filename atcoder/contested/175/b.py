N=int(input())
L=list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i]==L[j] or L[j]==L[k] or L[i]==L[k]:continue
            if abs(L[i] - L[j]) < L[k] < L[i]+L[j]:ans+=1
print(ans)