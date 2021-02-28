N,M=list(map(int,input().split()))
H=list(map(int,input().split()))
W=list(map(int,input().split()))
sum_list = [0]*((N+1)//2)
H.sort()
W.sort()
def search(h):
    left = 0
    right = M-1
    while right-left > 1:
        middle = (left+right)//2
        if W[middle] >= h:
            right = middle
        else:
            left = middle
    return left, right
for i in range((N+1)//2):
    sum_list[i+1] = H[i*2+1] - H[i*2] + sum_list[i]
ans = float('inf')
for i in range(H):
    h = H[i]
    l_index, r_index=search(h)
    left = W[l_index]
    right = W[r_index]
    if abs(h-left) >= abs(h-right):
        target_index = right if right%2==0 else left
    else:
        target_index = left if left%2==0 else right
    left_sum = 