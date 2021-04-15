N=int(input())
blue = {}
for _ in range(N):
    s = input().rstrip()
    if s in blue:
        blue[s]+=1
    else:
        blue[s]=1
M=int(input())
for _ in range(M):
    s = input().rstrip()
    if s in blue: 
        blue[s]-=1
ans = 0
for k,e in blue.items():
    ans=max(ans,e)
print(ans)