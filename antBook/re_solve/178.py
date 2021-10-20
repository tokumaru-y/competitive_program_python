# https://atcoder.jp/contests/abc175/tasks/abc175_b
N=int(input())
L=list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if len(list(set([L[i],L[j],L[k]]))) < 3:continue
            if abs(L[i]-L[j]) < L[k] < L[i]+L[j]:ans+=1
print(ans)