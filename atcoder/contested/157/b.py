bingo = [list(map(int,input().split())) for _ in range(3)]
N=int(input())
n = [[False] * 3 for _ in range(3)]
for _ in range(N):
    a = int(input())
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == a:n[i][j]=True
ans = False
for i in range(3):
    if n[i][0] and n[i][1] and n[i][2]:
        ans = True
for i in range(3):
    if n[0][i] and n[1][i] and n[2][i]:
        ans = True
for i in [0,2]:
    if n[0][i] and n[1][1] and n[2][2 if i==0 else 0]:
        ans = True
print("Yes" if ans else "No")