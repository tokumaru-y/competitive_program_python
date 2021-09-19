N,M=list(map(int, input().split()))
l_a = []
l_b = []
for i in range(M):
    a,b = list(map(int, input().split()))
    l_a.append([a,i])
    l_b.append([b,i])
l_a.sort()
l_b.sort()
used=[False] * M
ans = 0
pre_a = -1
pre_b = -1
for i in range(M):
    a,ai = l_a[i]
    b,bi = l_b[i]
    if used[ai] or used[bi]:continue
    if pre_a == a or pre_b == b:continue
    if pre_a >= a and pre_b <=b:continue
    if pre_b >= b and pre_a <=a:continue
    pre_a=a
    pre_b=b
    if a>=b:
        used[bi]=True
    else:
        used[ai]=True
    ans += 1
print(ans)