N=int(input())
S=list(map(int, input().split()))
T=list(map(int, input().split()))
sort_list = []
for i in range(N):
    sort_list.append([T[i], S[i], i])
sort_list = sorted(sort_list, key=lambda x:x[0])
ans = [float("inf")] * N
ind = sort_list[0][2]
total = sort_list[0][0]
for _ in range(N):
    t,s,i = T[ind], S[ind], ind
    if total< t:
        ans[ind] = total
    else:
        ans[ind]=t
        total=t
    total+=s
    if ind==N-1:
        ind=0
    else:
        ind+=1
print(*ans, sep="\n")