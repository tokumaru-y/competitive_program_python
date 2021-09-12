import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N=int(input())
XY=[list(map(int, input().split())) for _ in range(N)]
table = {}
XY=list(sorted(XY, key=lambda x:(x[0],x[1])))
pre = XY[0][0]
li = []
for x,y in XY:
    if x != pre:
        if len(li) >= 2:
            ll = len(li)
            for i in range(ll):
                for j in range(i+1,ll):
                    c = (li[i], li[j])
                    if c in table:
                        table[c] += 1
                    else:
                        table[c] = 1
        li = []
        pre = x
    li.append(y)
if len(li) >= 2:
    ll = len(li)
    for i in range(ll):
        for j in range(i+1,ll):
            c = (li[i], li[j])
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
ll = len(table)
ans = 0
tmp = [v for v in table.values()]
for i in range(ll):
    if tmp[i] < 2:continue
    ans+=combinations_count(tmp[i], 2)
print(ans)