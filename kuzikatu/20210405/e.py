N=int(input())
A=list(map(int, input().split()))
plus = []
minus = []
for a in A:
    if a >= 0:
        plus.append(a)
    else:
        minus.append(a)
plus.sort()
minus.sort()
# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_c
