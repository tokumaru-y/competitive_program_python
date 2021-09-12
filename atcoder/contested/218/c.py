
N=int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]


def rootate(S):
    return list(zip(*S[::-1]))

def find_top(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "#":
                return (i,j)


def check(S,T):
    sh, sw = find_top(S)
    th, tw = find_top(T)
    dif_h = th-sh
    dif_w = tw-sw
    for i in range(N):
        for j in range(N):
            nh = dif_h + i
            nw = dif_w + j
            if not (0<=nh<=N-1 and 0<=nw<=N-1):
                if S[i][j] == "#":return False
            else:
                if S[i][j] != T[nh][nw]:return False
    return True

cnt_s = 0
cnt_t = 0
for i in range(N):
    cnt_s += sum([1 if x=="#" else 0 for x in S[i]])
    cnt_t += sum([1 if x=="#" else 0 for x in T[i]])
if cnt_s != cnt_t:
    print("No")
    exit()
for _ in range(4):
    if check(S,T):
        print("Yes")
        exit()
    S=rootate(S)
print("No")