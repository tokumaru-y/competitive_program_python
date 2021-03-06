N=int(input())
L=input().rstrip()
ans = float('inf')
red = 0
for i in range(N):
    if L[i]=='R':
        red += 1
ans = red
white = 0
for i in range(N):
    if L[i]=='W':white+=1
    else:red-=1
    ans = min(ans,max(red,white))
print(ans)