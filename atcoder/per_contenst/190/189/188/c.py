n=int(input())
a=list(map(int,input().split()))
half=((2**n)-2)//2
left=max(a[:half+1])
right=max(a[half+1:])
if left>right:
    print(a.index(right)+1)
else:
    print(a.index(left)+1)