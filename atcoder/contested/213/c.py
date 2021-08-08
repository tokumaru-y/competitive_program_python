H,W,N=list(map(int, input().split()))
h_list = set()
w_list = set()
AB=[]
for _ in range(N):
    a,b=list(map(int, input().split()))
    h_list.add(a)
    w_list.add(b)
    AB.append([a,b])
h_list = sorted(list(h_list))
w_list = sorted(list(w_list))
ans_h = {}
ans_w = {}
ind = 1
for h in h_list:
    ans_h[h]=ind
    ind+=1
ind = 1
for w in w_list:
    ans_w[w]=ind
    ind+=1
for a,b in AB:
    print(ans_h[a],ans_w[b])