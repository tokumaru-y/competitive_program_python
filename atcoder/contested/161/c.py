N,K=list(map(int, input().split()))
div = N//K
print(min(abs(N-div*K), abs(N-(div+1)*K)))