from bisect import bisect_right,bisect_left
N,K=list(map(int, input().split()))
A=list(map(int,input().split()))
B=list(map(int, input().split()))
B.sort()
left = 0
right = 10**18
while right-left > 1:
    mid = (left+right)//2
    count = 0
    for a in A:
        w = mid // a
        count += bisect_right(B,w)
    if count >= K:
        right = mid
    else:
        left = mid
print(right)
