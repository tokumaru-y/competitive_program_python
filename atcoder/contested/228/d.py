Q=int(input())
N=1048576
TX=[list(map(int, input().split())) for _ in range(Q)]
used = [-1] * N
s_Tx = [(t,x%N,x) for t,x in TX]
s_TX = sorted(s_Tx, key=lambda x:x[1])
for t,idx,x in s_Tx:
    now_idx = idx
    if t == 1:
        while
    elif t == 2:
        print(used[idx])
