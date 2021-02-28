import bisect
N,M=list(map(int,input().split()))
H=list(map(int,input().split()))
W=list(map(int,input().split()))
pre_list = [0]*(N//2+1)
back_list = [0]*(N//2+1)
H.sort()
# W.sort()
for i in range(1,N//2):
    pre_list[i] = pre_list[i-1] + abs(H[2*i] -H[2*i+1]) if i!=0 else abs(H[0]-H[1])
    back_list[i] = back_list[i-1] + abs(H[N-1-2*i] - H[N-2-2*i]) if i != 0 else abs(H[N-1] - H[N-2])
ans = float('inf')
# print(pre_list)
# print(back_list)
for i in range(M):
    w = W[i]
    ind = bisect.bisect_left(H,w)
    # if ind == N:
    #     ind-=1
    # if ind == 0:
    #     tmp_sum = pre_list[ind//2-1]+back_list[(N//2)-(ind//2)-1]
    #     tmp_sum+= abs(w-H[ind])
    #     # print(i, tmp_sum,  ind)
    # else:
    ind1,ind2 = ind-1,ind+1
    comp1 = pre_list[ind1//2-1]+back_list[(N//2)-1-(ind1//2)]+abs(w-H[ind1]) if 0<= ind1 <= N-1 else float('inf')
    comp2 = pre_list[ind2//2-1]+back_list[(N//2)-1-(ind2//2)]+abs(w-H[ind2]) if 0<= ind2 <= N-1 else float('inf')
    tmp_sum = min(comp1,comp2)
    print(i,ind1,ind2,comp1,comp2)
    ans = min(ans, tmp_sum)
print(ans)