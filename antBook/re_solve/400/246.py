# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_c
N=int(input())
S=list(input())
black = 0
white = 0
for s in S:
    if s == ".":white += 1
ans = white + black
for s in S:
    if s == ".":
        white -= 1
    else:
        black += 1
    ans = min(ans, white+black)
print(ans)