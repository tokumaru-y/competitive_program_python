S=input().rstrip()
flag=True
Q=int(input())
pre = []
back = []
for _ in range(Q):
    q = input().split()
    if q[0]=='1':
        flag = not flag
    else:
        f,c = q[1], q[2]
        if f == '1':
            if flag:
                pre.append(c)
            else:
                back.append(c)
        else:
            if flag:
                back.append(c)
            else:
                pre.append(c)
pre.reverse()
S = ''.join(pre) + S + ''.join(back)
if not flag:
    S = S[::-1]
print(S)