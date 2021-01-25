a,b=input().split()
a_s=0
b_s=0
for i in range(3):
    a_s+=int(a[i])
    b_s+=int(b[i])
print(a_s if a_s>=b_s else b_s)