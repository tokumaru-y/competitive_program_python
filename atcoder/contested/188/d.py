N,C=list(map(int,input().split()))
ABC=[list(map(int,input().split())) for _ in range(N)]
events=[]
for a,b,c in ABC:
    events.append([a-1,c])
    events.append([b,-c])
events.sort()
ans=0
passed=0
money=0
for x,y in events:

    ans += min(C,money) * (x-passed)
    passed=x
    money += y
print(ans)