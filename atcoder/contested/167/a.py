S=input().rstrip()
T=input().rstrip()
ls= len(S)
for i in range(ls):
    if S[i] != T[i]:
        print("No")
        exit()
print("Yes")