N,M=list(map(int, input().split()))
al = (N+M)*(N+M-1)//2
print(al - N*M)