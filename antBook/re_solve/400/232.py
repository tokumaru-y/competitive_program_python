# https://atcoder.jp/contests/agc031/tasks/agc031_a
import string
import sys
sys.setrecursionlimit(10**9)
N=int(input())
S=input()
MOD = 10**9 + 7
table = {}
for a in string.ascii_lowercase:table[a] = 0
for i in range(N):
    table[S[i]] += 1
ans = 1
for a in string.ascii_lowercase:
    ans *= table[a] + 1
    ans %= MOD
print((ans + MOD - 1)%MOD) 