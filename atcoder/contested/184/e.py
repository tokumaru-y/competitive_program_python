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
while len(q) > 0:
    nex = heapq.heappop(q)
    cnt,n_h,n_w = nex
    for i in range(4):
        h_i = n_h+d_h[i]
        w_i = n_w+d_w[i]
        if not (0 <= h_i <= h-1 and 0 <= w_i <= w-1):continue
        if grid[h_i][w_i]=='#' or passed[h_i][w_i]:continue
        if h_i == e_h and w_i == e_w:
            ans=min(ans,cnt+1)
        if grid[h_i][w_i] == '.':
            heapq.heappush(q,[cnt+1,h_i,w_i])
        else:
            if grid[h_i][w_i] in h_table:
                if h_table[grid[h_i][w_i]] < cnt and not (grid[h_i][w_i] in checked):
                    heapq.heappush(q,[h_table[grid[h_i][w_i]]+1,h_i,w_i])
                    checked[grid[h_i][w_i]] = True
            else:
                heapq.heappush(q,[cnt+1,h_i,w_i])
                h_table[grid[h_i][w_i]] = cnt+1
        passed[h_i][w_i]=True
print(-1 if ans==float('inf') else ans)