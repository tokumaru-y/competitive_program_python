import math
R,B=list(map(int, input().split()))
x,y=list(map(int, input().split()))
left = 0
right = 10**19
while right - left > 1:
    mid=(left+right)//2
    if (R-mid)//(x-1) < 0 or (B-mid)//(y-1) < 0:
        right=mid
        continue
    a = (R-mid)//(x-1) + (B-mid)//(y-1)
    if a>=mid:
        left = mid
    else:
        right = mid
print(left)
