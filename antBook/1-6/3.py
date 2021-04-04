N,Y=list(map(int, input().split()))
for i in range(N+1):
    for j in range(N+1):
        left = Y - i*10**4 - j*5000
        cnt = N-i-j
        if cnt < 0 or left < 0:continue
        if left == cnt * 1000:
            print(i,j,cnt)
            exit()
print(-1,-1,-1)