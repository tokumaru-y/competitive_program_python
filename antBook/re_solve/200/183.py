# https://atcoder.jp/contests/arc029/tasks/arc029_1
from itertools import permutations
N = int(input())
M= [int(input()) for _ in range(N)]
ans = float('inf')
for bit in range(1<<N):
    a,b = 0,0
    for i in range(N):
        if bit & (1<<i):
            a+=M[i]
        else:
            b+=M[i]
    ans = min(ans, max(a,b))
print(ans)