N,M=list(map(int,input().split()))
A=list(map(int,input().split()))
for a in A:
    N -= a
print(N if N >=0 else -1)