X,K,D=list(map(int,input().split()))
X = abs(X)
cnt = X//D
if cnt >= K:
    print(min(abs(X+D*K), abs(X-D*K)))
else:
    left = K - cnt
    if left % 2 == 0:
        print(min(abs(X+D*cnt),abs(X-D*cnt)))
    else:
        print(min(abs(X-D*(cnt+1)), abs(X+D*(cnt+1))))
