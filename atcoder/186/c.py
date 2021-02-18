N=int(input())
ans=0
for i in range(1,N+1):
    e = oct(i)[2:]
    if '7' not in str(i) and '7' not in e:
        ans+= 1

print(ans)