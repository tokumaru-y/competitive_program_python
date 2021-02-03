import heapq

h,w=list(map(int,input().split()))
grid=[input().rstrip() for _ in range(h)]
h_table={}
checked={}
d_h=[1,0,-1,0]
d_w=[0,1,0,-1]
for h_i in range(h):
    for w_i in range(w):
        target=grid[h_i][w_i]
        if target=='S':
            s_h=h_i
            s_w=w_i
        elif target=='G':
            e_h=h_i
            e_w=w_i
q=[[0,s_h,s_w]]
passed=[[False] * w for _ in range(h)]
passed[s_h][s_w]=True
heapq.heapify(q)
ans = float('inf')
