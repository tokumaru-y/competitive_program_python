def dfs(x,y):
    if x>=y:
        return y-x
    if y%2==0:
        return 1+dfs(x,y//2)
    else:
        



x,y=list(map(int,input().split()))
ans=dfs(x,y)
print(ans)