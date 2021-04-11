N=input().rstrip()
tmp = N
ln = len(N)
flag = True
for i in range(ln):
    if not N[i] == N[ln-i-1]:
        flag = False
if flag:
    print("Yes")
    exit()
for i in range(ln):
    flag = True
    tmp = '0' + tmp
    for j in range(len(tmp)//2):
        if not tmp[j] == tmp[len(tmp)-j-1]:
            flag = False
    if flag:
        print("Yes")
        exit()
print("No")