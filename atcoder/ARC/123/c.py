T=int(input())
for _ in range(T):
    N=list(input())
    table = [4,1,1,1,2,2,2,3,3,3]
    tmp = 0
    ll = len(N)
    for i in reversed(range(ll)):
        target = int(N[i])
        if i == ll-1:
            tmp=table[target]
            continue
        if tmp < table[target]:
            tmp=min(tmp+3, table[target]+3)
    print(tmp)