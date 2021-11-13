# https://atcoder.jp/contests/abc085/tasks/abc085_d
N,H=list(map(int, input().split()))
a_list = []
b_list = []
for _ in range(N):
    a,b = list(map(int, input().split()))
    a_list.append(a)
    b_list.append(b)
a_list.sort(reverse=True)
b_list.sort(reverse=True)
ans = 0
for b in b_list:
    if a_list[0] >= b:
        ans += (H+a_list[0] - 1) // a_list[0]
        break
    H -= b
    ans += 1
    if H <= 0:break
else:
    ans += (H+a_list[0] - 1) // a_list[0]
print(ans)