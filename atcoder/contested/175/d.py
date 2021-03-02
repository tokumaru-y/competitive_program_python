N,K=list(map(int,input().split()))
P=list(map(lambda x : int(x)-1,input().split()))
C=list(map(int,input().split()))
ans = float('-inf')
for i in range(N):
    round_sum = 0
    round_points=[]
    x = i
    while True:
        x=P[x]
        round_points.append(C[x])
        round_sum+=C[x]
        if x==i:break

    tmp = 0
    size = len(round_points)
    for j in range(size):
        tmp += round_points[j]
        now = tmp
        if j+1 > K:break
        if round_sum>0:
            now += round_sum*((K-j-1)//size)
        ans = max(ans, now)

print(ans)