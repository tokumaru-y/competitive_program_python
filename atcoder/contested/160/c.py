K,N=list(map(int, input().split()))
A = list(map(int, input().split()))
dif = []
for i in range(N-1):
    dif.append(A[i+1] - A[i])
dif.append(K-A[-1] + A[0])
m = max(dif)
s = sum(dif)
print(s - m)