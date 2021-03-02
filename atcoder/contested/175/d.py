N,K=list(map(int,input().split()))
P=list(map(lambda x : int(x)-1,input().split()))
C=list(map(int,input().split()))
ans = 0
for i in range(N):
    round_sum = 0
    round_points=[]
    x = i
    while True:
        if P[x]==i:break
        round_points.append(C[x])
        x=P[x]
        round_sum+=C[x]
    tmp = 0
    size = len(round_points)
    for j in range(size):
        tmp += round_points[j]
        now = tmp
        if round_sum>0:
            now += round_sum*(size//K)
        ans = max(ans, now)

print(ans)