N,M=list(map(int,input().split()))
num = [-1] * N
for _ in range(M):
    s,c = list(map(int, input().split()))
    s -= 1
    if num[s] != -1 and num[s] != c:
        print(-1)
        exit()
    num[s] = c
if N==1:
    for i in range(10):
        if num[0] == i:
            print(i)
            exit()
    if num[0] == -1:
        print(0)
        exit()
else:
    start = 1*10**(N-1)
    for i in range(start,1*10**(N)):
        strnum = str(i)
        for j in range(N):
            if num[j] == -1:continue
            if int(strnum[j]) != num[j]:
                break
        else:
            print(i)
            exit()
print(-1)