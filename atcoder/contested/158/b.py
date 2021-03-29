N,A,B=list(map(int,input().split()))
cnt = N//(A+B)
ans = cnt * A
ans += min(A,N%(A+B))
print(ans)