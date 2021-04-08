N=1000 - int(input())
ans = 0
for m in [500,100,50,10,5,1]:
    cnt = N//m
    ans+=cnt
    N-=cnt*m
print(ans)