N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
left = 0
right=10**9
ans = float('inf')
while right - left > 1:
    tmp_sum = 0
    middle = (right+left)//2
    for a in A:
        tmp_sum+=(a//middle) -1
    if tmp_sum >K:
        right = middle
    else:
        left = middle 
    if tmp_sum > 0:
        ans = min(ans,tmp_sum)
print(ans)