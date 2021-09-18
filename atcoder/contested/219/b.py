S=[]
for _ in range(3):
    S.append(input())
l = list(input())
ans = ""
for i in l:
    x = int(i)
    ans+=S[x-1]
print(ans)