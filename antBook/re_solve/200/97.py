#  https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0583
import math
def gcd(n,m):
    if n<m:n,m=m,n
    if m == 0:
        return n
    return gcd(m, n%m)
N=int(input())
ans = []
num_list = list(map(int, input().split()))
res = 0
for n in num_list:
    res = gcd(res, n)
for i in range(1, int(math.sqrt(res) + 1) + 1):
    if res%i==0:
        ans.append(i)
        if i!=(res//i):ans.append(res//i)
ans=list(sorted(list(set(ans))))
print(*ans, sep="\n")