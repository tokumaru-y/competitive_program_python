S=input().rstrip()
index = 0
ls = len(S)
while ls > 0:
    if ls - 7 >= 0 and S[ls-7:ls] == 'dreamer':
        ls -= 7
        continue
    if ls-6 >= 0 and S[ls-6:ls] == 'eraser':
        ls -= 6
        continue
    if ls-5 >= 0:
        if S[ls-5:ls] == 'dream' or S[ls-5:ls] == 'erase':
            ls -= 5
            continue
    print("NO")
    exit()
print("YES")