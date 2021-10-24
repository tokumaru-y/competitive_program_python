N=int(input())
d = {}
for _ in range(N):
    s=input()
    if d.get(s):
        d[s]+= 1
    else:
        d[s] = 1
M=int(input())
for _ in range(M):
    s=input()
    if d.get(s):
        d[s] -=1
    else:
        d[s] = -1
ans = 0
for key, value in d.items():
    ans = max(ans, value)
print(ans)