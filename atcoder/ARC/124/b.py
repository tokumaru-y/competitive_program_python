from bisect import bisect_left,bisect_right
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
B.sort()
a=A[0]
ans = 0
ans_list = []
tmp_dict = {}
for i in range(N):
    target = a^B[i]
    tmp_b = B[:]
    tmp_b.pop(i)
    is_ok = True
    for j in range(1,N):
        search = target^A[j]
        ind = bisect_left(tmp_b, search)
        if ind == len(tmp_b):
            is_ok = False
            break
        if tmp_b[ind] != search:
            is_ok = False
            break
        tmp_b.pop(ind)
    if is_ok and tmp_dict.get(target) is None:
        ans+= 1
        ans_list.append(target)
        tmp_dict[target] = 1
print(ans)
ans_list = sorted(list(set(ans_list)))
if ans > 0:
    print(*ans_list, sep="\n")