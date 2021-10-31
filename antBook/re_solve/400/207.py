# https://atcoder.jp/contests/abc083/tasks/arc088_a
X,Y=list(map(int, input().split()))
ans = 1
num = X
while True:
    num *= 2
    if num <= Y:
        ans += 1
    else:
        break
print(ans)