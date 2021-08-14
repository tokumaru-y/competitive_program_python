ans = 0
S,T=list(map(int, input().split()))
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a+b+c<=S and a*b*c<=T:ans+=1
print(ans)