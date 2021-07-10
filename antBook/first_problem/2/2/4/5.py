N=int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key = lambda x: -x[1])
CD = sorted(CD, key = lambda x: x[0])
used = [False] * N
ans = 0
for c,d in CD:
    tmp_list = []
    for i, l in enumerate(AB):
        a,b = l
        if not used[i] and c > a and d > b:
            tmp_list.append([b,a,i])
    if len(tmp_list) > 0:
        tmp_list.sort(reverse=True)
        b,a,i =tmp_list[0]
        used[i] = True
        ans += 1
print(ans)