from bisect import bisect_left,bisect_right
D=int(input())
N=int(input())
M=int(input())
shop=[0]*(N+1)
for i in range(1,N):
    shop[i]=int(input())
shop.append(D)
ans = 0
shop.sort()
for _ in range(M):
    d = int(input())
    ind=bisect_left(shop,d)
    ans += min(abs(shop[ind]-d), abs(shop[ind-1]-d))
print(ans)