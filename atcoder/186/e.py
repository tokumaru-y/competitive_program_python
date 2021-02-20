import math
T=int(input())
for _ in range(T):
    N,S,K=list(map(int,input().split()))
    g = math.gcd(K,N)
    if (S%g!=0):
        print(-1)
        continue
    N//=g
    S//=g
    K//=g
    p=pow(K,-1,N)
    print((-S*p)%N)