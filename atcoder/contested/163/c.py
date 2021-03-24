N=int(input())
ans = [0] * N
ll = list(map(int,input().split()))
for l in ll:
    ans[l-1]+=1
print(*ans, sep='\n')