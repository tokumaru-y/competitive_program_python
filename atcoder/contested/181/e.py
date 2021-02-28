import bisect
N,M=list(map(int,input().split()))
H=list(map(int,input().split()))
W=list(map(int,input().split()))
pre_list = [0]*(N//2)
back_list = [0]*(N//2)
H.sort()
# W.sort()
for i in range(2,N,2):
    pre_list[i-2] = pre_list[i-1] + abs(H[i+1] -H[i])
    back_list[i-2] = back_list[i-1] + abs(H[N-i] - H[N-i-1])
ans = float('inf')
print(pre_list)
print(back_list)
for i in range(M):
    w = W[i]
    ind = bisect.bisect_left(H,w)
    if ind % 2 ==1:continue
    print(ind)
    tmp_sum = pre_list[ind//2-1]+back_list[(N//2)-1-(ind//2)]
    tmp_sum+= abs(w-H[ind])
    ans = min(ans, tmp_sum)
print(ans)