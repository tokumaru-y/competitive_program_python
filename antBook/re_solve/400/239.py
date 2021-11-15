# https://atcoder.jp/contests/abc042/tasks/abc042_b
N,L=list(map(int, input().split()))
S = [input() for _ in range(N)]
S.sort()
print("".join(S))