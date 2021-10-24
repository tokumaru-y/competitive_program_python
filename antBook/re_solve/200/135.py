# https://atcoder.jp/contests/agc026/tasks/agc026_c
from bisect import bisect_left
N=int(input())
S=input()
half = []
ans = 0
for i in range(1<<N):
    red = ""
    blue = ""
    for j in range(N):
        if i & 1<<j:
            red += S[j]
        else:
            blue += S[j]
    half.append([red, blue])
half.sort()
for i in range(1<<N):
    red = ""
    blue = ""
    for j in range(N):
        if i & 1<<j:
            red += S[N+j]
        else:
            blue += S[N+j]
    idx = bisect_left(half, [blue, red])
    if idx <= len(half)-1:
        if red + half[idx][1] == "".join(list(reversed(blue+half[idx][0]))):ans+=1
print(ans)