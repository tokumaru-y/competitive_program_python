N,K=list(map(int ,input().split()))
sum_list = [K]*N
right_list = [0]*(N+1)
left_list = [0]*(N+1)
for _ in range(K):
    inp = list(input().split())
    s, ind = inp[0], inp[1]
    ind = int(ind)
    if s == "L":
        left_list[ind-1] -= 1
        sum_list[ind-1]=1
    else:
        right_list[ind] -= 1
        sum_list[ind-1] = 1
# print(sum_list)
for i in range(N):
    right_list[i+1] +=  right_list[i]  
for i in reversed(range(N)):
    left_list[i] += left_list[i+1]

# print(left_list)
# print(right_list)
ans = 1
MOD = 998244353
for i in range(N):
    if sum_list[i] == 1:
        ans *= 1
        continue
    ans *= K + right_list[i+1]+left_list[i+1]
    ans %=MOD
print(ans)