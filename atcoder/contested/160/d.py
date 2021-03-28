from collections import deque
N,X,Y = list(map(int, input().split()))
cnt = {}
for i in range(1,N):
    for j in range(i+1,N+1):
        tmp = min(j-i,abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))
        if tmp in cnt:
            cnt[tmp]+=1
        else:
            cnt[tmp]=1
for k in range(1,N):
    if k in cnt:
        print(cnt[k])
    else:
        print(0)