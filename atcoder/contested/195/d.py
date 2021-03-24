N,M,Q = list(map(int,input().split()))
VW = []
for _ in range(N):
    w,v=list(map(int,input().split()))
    VW.append([v,w])
VW = sorted(VW, key = lambda x : (x[0], x[1]), reverse=True)
Box = list(map(int,input().split()))
for _ in range(Q):
    left, right = list(map(lambda x:int(x) - 1,input().split()))
    box = Box[:left] + Box[right+1:]
    box.sort()
    used=[False]*(M-(right-left+1))
    ans = 0
    for v,w in VW:
        for i in range(M-right+left-1):
            if used[i]:continue
            if box[i]>=w:
                used[i]=True
                ans+=v
                break
    print(ans)