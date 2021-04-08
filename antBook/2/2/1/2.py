N,M=list(map(int, input().split()))
coins = list(map(int, input().split()))
coins.sort()
coins = coins[1:]
ans = float('inf')
for bit in range(1<<(M-1)):
    tmp_cnt = 0
    left = N
    for j in reversed(range(M-1)):
        if bit & 1<<j:
            cnt = left//coins[j]
            left -= coins[j] * cnt
            tmp_cnt += cnt
    tmp_cnt += left
    ans=min(ans, tmp_cnt)
print(coins, len(coins))
print(ans)
