N=int(input())
origin = N
S=list(map(int, input().split()))
T=list(map(int, input().split()))
ans = [0]*N
start_index = 0
tmp_num = float("inf")
for t in range(N):
    if tmp_num > T[t]:
        tmp_num = T[t]
        start_index = t
next_time = 0
ind = start_index
while N>0:
    N-=1
    if ind == start_index:
        ans[ind] = T[ind]
        next_time = T[ind] + S[ind]
    else:
        if next_time > T[ind]:
            next_time = T[ind]
        ans[ind] = next_time
        next_time += S[ind]
    ind += 1
    if ind == origin:
        ind = 0
# for i in range(N):
#     if i == 0:
#         ans[i]=T[i]
#         next_time += T[i] + S[i]
#     else:
#         if next_time > T[i]:
#             ans[i] = T[i]
#             next_time=T[i]
#         else:
#             ans[i] = next_time
#         next_time+=S[i]
print(*ans, sep="\n")