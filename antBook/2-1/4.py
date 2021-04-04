N=int(input())
t=[int(input()) for _ in range(N)]
ans = float('inf')
for bit in range(1<<N):
    a,b=0,0
    for i in range(N):
        if bit & 1<<i:
            a+=t[i]
        else:
            b+=t[i]
    ans = min(ans, max(a,b))
print(ans)