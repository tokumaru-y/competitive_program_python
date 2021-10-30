N,Q=list(map(int,input().split()))
query = [list(map(int, input().split())) for _ in range(Q)]
parents = [-1] * N
child = [-1] * N
import sys
sys.setrecursionlimit(10**9)
def s_parent(p,list):
    if parents[p] != -1:
        list.append(parents[p]+1)
        list = s_parent(parents[p], list)
    return list
def s_child(c,list):
    if child[c] != -1:
        list.append(child[c]+1)
        list = s_child(child[c], list)
    return list
for q in query:
    if q[0] == 1:
        # join
        _,x,y = q
        parents[y-1] = x-1
        child[x-1] = y-1
    elif q[0] == 2:
        # deattach
        _,x,y = q
        parents[y-1] = -1
        child[x-1] = -1
    elif q[0] == 3:
        # print
        _,x =q
        x-=1
        res = [x+1]
        p_list = []
        c_list = []
        if parents[x] != -1:
            p_list = s_parent(parents[x], [parents[x]+1])
            p_list.reverse()
        if child[x] != -1:
            c_list = s_child(child[x], [child[x]+1])
        res = p_list + res + c_list
        print(len(res), *res)