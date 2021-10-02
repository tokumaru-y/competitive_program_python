S=list(input())
T=list(input())
cnt=0
for i in range(len(S)):
    if S[i] != T[i] and i < len(S)-1:
        a = S[:]
        a[i],a[i+1]=a[i+1],a[i]
        if a == T:
            print("Yes")
            exit()
print("No" if S != T else "Yes")