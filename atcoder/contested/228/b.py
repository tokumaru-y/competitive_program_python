import sys
sys.setrecursionlimit(10**9)
N,X=list(map(int, input().split()))
X-=1
A=list(map(int, input().split()))
passed = [False] * N
ans = 0
def dfs(x):
    if not passed[x]:
        passed[x]= True
        global ans
        ans += 1
        dfs(A[x]-1)
dfs(X)
print(ans)