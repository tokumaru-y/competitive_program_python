N=int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]
hx=[0,1,0,-1]
wx=[1,0,-1,0]
for i in range(N):
    tmp = []
    lll = []
    if i == 1:
        # 90
        for h in range(N):
            t=[]
            for w in range(N):
                if T[w][h] == "#":
                    lll.append([h,w])
                t.append(T[w][h])
            tmp.append(t)
    elif i == 2:
        for h in range(N):
            t=[]
            for w in range(N):
                if T[-h][w] == "#":
                    lll.append([h,w])
                t.append(T[-h][w])
            tmp.append(t)
    elif i == 3:
        for h in range(N):
            t=[]
            for w in range(N):
                if T[w][-h] == "#":
                    lll.append([h,w])
                t.append(T[w][-h])
            tmp.append(t)
    else:
        tmp = T
    for h in range(N):
        for w in range(N):
            if S[h][w] == "#":
                for target in lll:
                    dh = h-target[0]
                    dw = w-target[1]
                    for th,tw in lll:
                        gh=th+dh
                        gw=tw+dw
                        if not(0<=gh<=N-1 and 0<=gw<=N-1):
                            break
                        if tmp[gh][gw] != "#":
                            break
                else:
                    print("Yes")
                    exit()
print("No")