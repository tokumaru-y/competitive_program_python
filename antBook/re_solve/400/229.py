# https://atcoder.jp/contests/abc089/tasks/abc089_c
from collections import defaultdict
N=int(input())
ll = ["M", "A", "R", "C", "H"]
table = {"M":0, "A":0,"R":0, "C":0,"H": 0}
for _ in range(N):
    s=input()
    if s[0] in ll:
        table[s[0]]+=1
from itertools import combinations
ans = 0
for p in combinations(table.values(), 3):
    if not all(p):continue
    ans += (p[0] * p[1] * p[2])
print(ans)