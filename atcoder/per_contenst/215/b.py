N=int(input())
ans = 0
tmp = 1
while tmp<=N:
    ans += 1
    tmp *= 2
print(ans-1)