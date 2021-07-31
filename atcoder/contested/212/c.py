N,M=list(map(int, input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))
A.sort()
B.sort()
ans = float("inf")
from bisect import bisect_left
for a in A:
    ind = bisect_left(B,a)
    if ind == M:
        ans = min(ans, abs(a-B[ind-1]))
    elif ind > 0:
        ans = min(ans, abs(a-B[ind]), abs(a-B[ind-1]))
    else:
        ans = min(ans, abs(a-B[ind]))
print(ans)