# https://atcoder.jp/contests/abc103/tasks/abc103_d
N,M=list(map(int,input().split()))
AB=[list(map(int, input().split())) for _ in range(M)]
sorted_AB = sorted(AB, key=lambda x:[x[1],x[0]])
ans = 0
right = float("-inf")
for a,b in sorted_AB:
    if right < a:
        ans += 1
        right = b
print(ans)