N,M=list(map(int, input().split()))
AB=[]
for _ in range(M):
    a,b=list(map(lambda x :int(x)-1, input().split()))
    AB.append([b,a])
AB.sort()
ans = 0
limit = 0
for b,a in AB:
    if a > limit:
        limit = b-1
        ans +=1
print(ans)