from collections import defaultdict
H,W,N=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
Hs = []
Ws = []
for a,b in AB:
    Hs.append(a)
    Ws.append(b)
h_dict = {x:i+1 for i, x in enumerate(sorted(list(set(Hs))))}
w_dict = {y:i+1 for i, y in enumerate(sorted(list(set(Ws))))}
for a,b in AB:
    print(h_dict[a], w_dict[b])