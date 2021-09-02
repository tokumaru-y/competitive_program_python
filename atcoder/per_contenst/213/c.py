from bisect import bisect_left
N,M=list(map(int, input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))
B.sort()
ans = float("inf")
for a in A:
    ind = bisect_left(B,a)
    if ind == M:ind-=1
    ans = min(ans, abs(a-B[ind]))
    if ind > 0:ans=min(ans, abs(a-B[ind-1]))
    if ind < M-1:ans=min(ans,abs(a-B[ind+1]))
print(ans)
