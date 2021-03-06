N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
left = 0
right=10**9
ans = float('inf')
def search(length):
    cnt = 0
    for a in A:
        cnt += (a-1)//length
    return cnt <= K

while right - left > 1:
    middle = (right+left)//2
    if search(middle):
        right = middle
    else:
        left = middle
print(right)