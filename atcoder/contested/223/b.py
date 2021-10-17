S=input()
ans1 = S
ans2 = S
for i in range(len(S)):
    tmp = S[1:] + S[0]
    ans1=min(ans1, tmp)
    ans2=max(ans2, tmp)
    S = tmp
print(ans1)
print(ans2)