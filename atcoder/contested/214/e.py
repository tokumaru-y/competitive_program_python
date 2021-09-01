from heapq import heapify,heappop,heappush
T=int(input())
for _ in range(T):
    N=int(input())
    LR = [list(map(int ,input().split())) for _ in range(N)]
    l_list = []
    dic = {}
    for l,r in LR:
        if l in dic:
            dic[l].append(r)
        else:
            dic[l] = [r]
        l_list.append(l)
    l_list.sort(reverse=True)
    h = []
    heapify(h)
    ind = 0
    is_ok = True
    while len(l_list) > 0:
        target = l_list.pop()
        if ind<target:
            ind=target
        for dic_num in dic[target]:
            
            h.append(dic_num)
        while len(h)>0:
            min_n = h.pop()
            if min_n > ind:
                is_ok=False
                break
            ind+=1
    if is_ok:
        print("Yes")
    else:
        print("No")
        