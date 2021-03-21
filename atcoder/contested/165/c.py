N,M,Q=list(map(int,input().split()))
A=[0]*Q
B=[0]*Q
C=[0]*Q
D=[0]*Q
for i in range(Q):
    A[i],B[i],C[i],D[i]=list(map(int, input().split()))
    A[i]-=1
    B[i]-=1

def dfs(List):
    if len(List) == N:
        tmp_cnt = 0
        for a,b,c,d in zip(A,B,C,D):
            if List[b] - List[a] == c:
                tmp_cnt+=d
        return tmp_cnt

    start = 0 if len(List) == 0 else List[-1]
    res = 0
    for i in range(start, M):
        List.append(i)
        res = max(res, dfs(List))
        List.pop()
    return res

ans = dfs([])
print(ans)