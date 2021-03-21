N,K=list(map(int,input().split()))
snuke = [False]*N
for _ in range(K):
    d=int(input())
    s = list(map(int,input().split()))
    for ss in s:
        snuke[ss-1] = True
print(snuke.count(False))