N=input().rstrip()
s = 0
for n in N:
    s+=int(n)
print("Yes" if s%9==0 else "No")