S=input().rstrip()
T=input().rstrip()
lens=len(S)
lent=len(T)
ans = lent
for i in range(lens-lent+1):
    tmp = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            tmp+=1
    ans = min(ans, tmp)
print(ans)