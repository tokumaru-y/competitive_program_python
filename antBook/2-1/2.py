A = input().rstrip()
for bit in range(1<<3):
    ans = A[0]
    cnt = int(A[0])
    for i in range(3):
        if bit & 1<<i:
            cnt += int(A[i+1])
            ans += '+'+A[i+1]
        else:
            cnt -= int(A[i+1])
            ans += '-'+A[i+1]
    if cnt == 7:
        print(ans + '=7')
        exit()