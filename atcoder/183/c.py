from itertools import permutations
N,K=list(map(int,input().split()))
times = [list(map(int,input().split())) for _ in range(N)]
passed=[False] * N
ans= 0
def dfs(t,value):
    if passed.count(True) == N:
        if value + times[t][0] == K:
            global ans
            ans+=1
        return value + times[t][0]
    res = float('inf')
    for i in range(N):
        if passed[i]:continue
        passed[i]=True
        res =(res,dfs(i,value+times[t][i]))
        passed[i]=False
    return res
passed[0]=True
dfs(0,0)
print(ans)