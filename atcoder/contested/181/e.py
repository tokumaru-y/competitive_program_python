import bisect
N,M=list(map(int,input().split()))
H=list(map(int,input().split()))
W=list(map(int,input().split()))
pre_list = [0]*(N+1)
back_list = [0]*(N+1)
H.sort()
for i in range(2, N, 2):
    pre_list[i] = pre_list[i-2] + H[i-1] - H[i-2]
    back_list[i] = back_list[i-2] + H[N-i+1] - H[N-i]
ans = float('inf')
for w in W:
    ind = bisect.bisect_left(H,w)
    if ind%2==0:
        ans = min(ans, pre_list[ind] + back_list[N-ind-1] + abs(w-H[ind]))
    else:
        ans = min(ans, pre_list[ind-1] + back_list[N-ind] + abs(w-H[ind-1]))
print(ans)