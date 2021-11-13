N,K,A=list(map(int, input().split()))
now = A-1
while K > 0:
    now += 1
    K -= 1
    if K == 0:
        print(now)
        exit()
    if now == N:now = 0