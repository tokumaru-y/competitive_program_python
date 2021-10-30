N,M=list(map(int, input().split()))
B=[list(map(int, input().split())) for _ in range(N)]
start = B[0][0]
div_h = start // 7
div_w = start % 7
if not (0<=div_h<=10**100 and div_w <= 6):
    print("No")
    exit()
if (div_w == 0 and M > 1) or div_w + M >= 9:
    print("No")
    exit()
for h in range(N):
    for w in range(M):
        if h == 0 and w == 0:continue
        if B[h][w] != start + w:
            print("No")
            exit()
    start += 7
print("Yes")